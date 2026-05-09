#!/usr/bin/env node
// Exports the deck as a PDF: proxies Google Fonts through Node,
// scrolls to each slide and screenshots it, combines with pdf-lib.
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
  const key  = Buffer.from(url).toString('base64').replace(/\//g, '_').slice(-80);
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
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });

  // Proxy Google Fonts through Node so headless Chrome gets real fonts
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

  // Activate print layout using setProperty so existing inline styles are preserved
  const slideCount = await page.evaluate(() => {
    const stage = document.querySelector('deck-stage');
    if (stage) {
      stage.style.display   = 'block';
      stage.style.position  = 'static';
      stage.style.width     = '1920px';
      stage.style.height    = 'auto';
      stage.style.overflow  = 'visible';
      stage.style.transform = 'none';
    }
    const slides = document.querySelectorAll('section.slide');
    slides.forEach(s => {
      s.style.setProperty('position',  'relative', 'important');
      s.style.setProperty('display',   'block',    'important');
      s.style.setProperty('width',     '1920px',   'important');
      s.style.setProperty('height',    '1080px',   'important');
      s.style.setProperty('transform', 'none',     'important');
      s.style.setProperty('overflow',  'hidden',   'important');
      s.style.setProperty('margin',    '0',        'important');
      s.style.setProperty('padding',   '0',        'important');
      s.style.setProperty('float',     'none',     'important');
    });
    return slides.length;
  });

  await new Promise(r => setTimeout(r, 400));
  console.log(`Found ${slideCount} slides — capturing...`);

  const pngs = [];
  for (let i = 0; i < slideCount; i++) {
    // Scroll to this slide's position
    await page.evaluate((y) => window.scrollTo(0, y), i * H);
    await new Promise(r => setTimeout(r, 200));

    const png = await page.screenshot({ type: 'png' });
    pngs.push(png);
    process.stdout.write(`  ✓ ${i + 1}/${slideCount}\r`);
  }
  console.log(`\nBuilding PDF...`);

  await browser.close();

  const pdf = await PDFDocument.create();
  for (const png of pngs) {
    const img     = await pdf.embedPng(png);
    const pdfPage = pdf.addPage([W, H]);
    pdfPage.drawImage(img, { x: 0, y: 0, width: W, height: H });
  }

  const bytes = await pdf.save();
  fs.writeFileSync(OUT, bytes);
  const mb = (fs.statSync(OUT).size / 1024 / 1024).toFixed(1);
  console.log(`✓ carousel-deck.pdf  (${mb} MB)  →  ${OUT}`);
})();
