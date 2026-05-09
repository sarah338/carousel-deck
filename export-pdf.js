#!/usr/bin/env node
// Exports the deck as a PDF.
// Strategy: proxy Google Fonts through Node (Chrome can't reach them but Node can),
// activate the deck's print layout, screenshot each slide, combine into PDF.
const puppeteer = require('puppeteer');
const { PDFDocument } = require('pdf-lib');
const https = require('https');
const path  = require('path');
const fs    = require('fs');

const W   = 1920;
const H   = 1080;
const HTML = `file://${path.join(__dirname, 'index.html')}`;
const OUT  = path.join(__dirname, 'carousel-deck.pdf');
const CACHE_DIR = path.join(__dirname, '.font-cache');

// ── Font proxy ────────────────────────────────────────────────────────────────

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
  const key  = url.replace(/[^a-z0-9]/gi, '_').slice(-80);
  const file = path.join(CACHE_DIR, key);
  if (fs.existsSync(file)) return fs.readFileSync(file);
  const buf = await fetchBuffer(url);
  fs.writeFileSync(file, buf);
  return buf;
}

// ── Main ──────────────────────────────────────────────────────────────────────

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--no-sandbox', '--disable-setuid-sandbox',
      '--font-render-hinting=none',
      '--disable-web-security',
    ],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 2 });

  // Proxy all Google Fonts requests through Node so Chrome gets real fonts
  await page.setRequestInterception(true);
  page.on('request', async req => {
    const u = req.url();
    if (u.includes('fonts.googleapis.com') || u.includes('fonts.gstatic.com')) {
      try {
        const buf = await cachedFetch(u);
        const ct  = u.includes('.ttf')   ? 'font/truetype'
                  : u.includes('.woff2') ? 'font/woff2'
                  : u.includes('.woff')  ? 'font/woff'
                  : 'text/css; charset=utf-8';
        req.respond({ status: 200, contentType: ct, body: buf });
      } catch (e) {
        req.abort();
      }
    } else {
      req.continue();
    }
  });

  await page.goto(HTML, { waitUntil: 'networkidle0' });
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 800));

  // Activate print layout — set individual properties to preserve existing styles
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
      s.style.setProperty('position',            'relative', 'important');
      s.style.setProperty('display',             'block',    'important');
      s.style.setProperty('width',               '1920px',   'important');
      s.style.setProperty('height',              '1080px',   'important');
      s.style.setProperty('transform',           'none',     'important');
      s.style.setProperty('overflow',            'hidden',   'important');
      s.style.setProperty('margin',              '0',        'important');
      s.style.setProperty('print-color-adjust',  'exact',    'important');
      s.style.setProperty('-webkit-print-color-adjust', 'exact', 'important');
    });
    return slides.length;
  });

  await new Promise(r => setTimeout(r, 400));
  console.log(`Found ${slideCount} slides — capturing screenshots...`);

  // Screenshot each slide by clipping at its y-offset
  const pngs = [];
  for (let i = 0; i < slideCount; i++) {
    const png = await page.screenshot({
      type: 'png',
      clip: { x: 0, y: i * H, width: W, height: H },
    });
    pngs.push(png);
    process.stdout.write(`  ✓ ${i + 1}/${slideCount}\n`);
  }

  await browser.close();

  // Combine PNGs into PDF with pdf-lib
  console.log('Building PDF...');
  const pdf = await PDFDocument.create();
  for (const png of pngs) {
    const img  = await pdf.embedPng(png);
    const page = pdf.addPage([W, H]);
    page.drawImage(img, { x: 0, y: 0, width: W, height: H });
  }

  const bytes = await pdf.save();
  fs.writeFileSync(OUT, bytes);
  const mb = (fs.statSync(OUT).size / 1024 / 1024).toFixed(1);
  console.log(`✓ carousel-deck.pdf  (${mb} MB)  →  ${OUT}`);
})();
