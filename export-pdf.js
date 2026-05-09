#!/usr/bin/env node
// Exports the deck as a pixel-perfect PDF with embedded fonts.
// On first run, downloads fonts from Google and caches them locally.
const puppeteer = require('puppeteer');
const https = require('https');
const path = require('path');
const fs = require('fs');

const W = 1920;
const H = 1080;
const HTML      = `file://${path.join(__dirname, 'index.html')}`;
const OUT       = path.join(__dirname, 'carousel-deck.pdf');
const FONT_CACHE = path.join(__dirname, '.font-cache.css');
const FONTS_URL = 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@200;300;400;500&display=swap';

function get(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)' } }, res => {
      if (res.statusCode >= 300 && res.headers.location)
        return get(res.headers.location).then(resolve).catch(reject);
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => resolve(Buffer.concat(chunks)));
      res.on('error', reject);
    }).on('error', reject);
  });
}

async function buildFontCSS() {
  if (fs.existsSync(FONT_CACHE)) {
    console.log('Fonts: using cache');
    return fs.readFileSync(FONT_CACHE, 'utf8');
  }
  console.log('Fonts: downloading from Google...');
  let css = (await get(FONTS_URL)).toString();
  const urls = [...css.matchAll(/url\((https:\/\/[^)]+)\)/g)].map(m => m[1]);
  for (const url of urls) {
    const buf = await get(url);
    css = css.replace(url, `data:font/woff2;base64,${buf.toString('base64')}`);
    process.stdout.write('.');
  }
  console.log(` ${urls.length} files embedded`);
  fs.writeFileSync(FONT_CACHE, css);
  return css;
}

(async () => {
  const fontCSS = await buildFontCSS();

  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 2 });

  // Block Google Fonts requests — we'll inject them embedded instead
  await page.setRequestInterception(true);
  page.on('request', req => {
    if (req.url().includes('fonts.googleapis') || req.url().includes('fonts.gstatic'))
      req.abort();
    else
      req.continue();
  });

  await page.goto(HTML, { waitUntil: 'domcontentloaded' });
  await new Promise(r => setTimeout(r, 400));

  // Swap Google Fonts link for embedded fonts
  await page.evaluate(css => {
    document.querySelectorAll('link[href*="fonts.googleapis"]').forEach(l => l.remove());
    const s = document.createElement('style');
    s.textContent = css;
    document.head.insertBefore(s, document.head.firstChild);
  }, fontCSS);

  // Activate print layout (same logic as the deck's own beforeprint handler)
  await page.evaluate(() => {
    const stage = document.querySelector('deck-stage');
    if (stage) stage.style.cssText =
      'display:block;position:static;width:1920px;height:auto;overflow:visible;transform:none;';
    document.querySelectorAll('section.slide').forEach(s => {
      const bg    = s.style.background || s.style.backgroundColor || '';
      const color = s.style.color || '';
      s.style.cssText =
        'position:relative!important;display:block!important;' +
        'width:1920px!important;height:1080px!important;' +
        'transform:none!important;break-after:page!important;overflow:hidden!important;';
      if (bg)    s.style.background = bg;
      if (color) s.style.color = color;
    });
  });

  await page.emulateMediaType('print');
  await new Promise(r => setTimeout(r, 600));

  await page.pdf({
    path: OUT,
    width: `${W}px`,
    height: `${H}px`,
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
  });

  await browser.close();
  const mb = (fs.statSync(OUT).size / 1024 / 1024).toFixed(1);
  console.log(`✓ carousel-deck.pdf  (${mb} MB)  →  ${OUT}`);
})();
