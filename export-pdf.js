#!/usr/bin/env node
// Uses deck-stage's own goTo() API to navigate each slide,
// proxies Google Fonts through Node, screenshots, combines into PDF.
const puppeteer  = require('puppeteer');
const { PDFDocument } = require('pdf-lib');
const https = require('https');
const path  = require('path');
const fs    = require('fs');

const W    = 1920;
const H    = 1080;
const HTML = `file://${path.join(__dirname, 'index.html')}`;
const OUT  = path.join(__dirname, 'carousel-deck.pdf');
const CACHE_DIR = path.join(__dirname, '.font-cache');

function fetchBuffer(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)' } }, res => {
      if (res.statusCode >= 300 && res.headers.location)
        return fetchBuffer(res.headers.location).then(resolve).catch(reject);
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => resolve(Buffer.concat(chunks)));
      res.on('error', reject);
    }).on('error', reject);
  });
}

async function cachedFetch(url) {
  fs.mkdirSync(CACHE_DIR, { recursive: true });
  const key  = Buffer.from(url).toString('base64').replace(/[/+=]/g, '_').slice(-80);
  const file = path.join(CACHE_DIR, key);
  if (fs.existsSync(file)) return fs.readFileSync(file);
  const buf = await fetchBuffer(url);
  fs.writeFileSync(file, buf);
  return buf;
}

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none'],
  });

  const page = await browser.newPage();
  // Match the deck's design size exactly so scale = 1.0
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 2 });

  // Proxy Google Fonts through Node (headless Chrome can't reach them directly)
  await page.setRequestInterception(true);
  page.on('request', async req => {
    const u = req.url();
    if (u.includes('fonts.googleapis.com') || u.includes('fonts.gstatic.com')) {
      try {
        const buf = await cachedFetch(u);
        const ct  = u.includes('.ttf')   ? 'font/truetype'
                  : u.includes('.woff2') ? 'font/woff2'
                  : 'text/css; charset=utf-8';
        req.respond({ status: 200, contentType: ct, body: buf });
      } catch { req.abort(); }
    } else {
      req.continue();
    }
  });

  await page.goto(HTML, { waitUntil: 'networkidle0' });
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 1000));

  // deck-stage exposes goTo(i) and .length
  const slideCount = await page.evaluate(() =>
    document.querySelector('deck-stage').length
  );
  console.log(`Found ${slideCount} slides — capturing...`);

  const pngs = [];
  for (let i = 0; i < slideCount; i++) {
    // Use the deck's own API — handles visibility, opacity, everything
    await page.evaluate((idx) => document.querySelector('deck-stage').goTo(idx), i);
    await new Promise(r => setTimeout(r, 350));
    pngs.push(await page.screenshot({ type: 'png' }));
    process.stdout.write(`  ✓ ${i + 1}/${slideCount}\r`);
  }

  await browser.close();
  console.log('\nBuilding PDF...');

  const pdf = await PDFDocument.create();
  for (const png of pngs) {
    const img     = await pdf.embedPng(png);
    const pdfPage = pdf.addPage([W, H]);
    pdfPage.drawImage(img, { x: 0, y: 0, width: W, height: H });
  }

  fs.writeFileSync(OUT, await pdf.save());
  const mb = (fs.statSync(OUT).size / 1024 / 1024).toFixed(1);
  console.log(`✓ carousel-deck.pdf  (${mb} MB)  →  ${OUT}`);
})();
