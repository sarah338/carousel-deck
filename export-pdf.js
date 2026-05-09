#!/usr/bin/env node
// Exports each slide as a full-bleed 1920x1080 PNG, then combines into a PDF.
const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const SLIDE_W = 1920;
const SLIDE_H = 1080;
const OUT_DIR = path.join(__dirname, 'pdf-export');
const HTML_PATH = path.join(__dirname, 'index.html');
const PDF_OUT = path.join(__dirname, 'carousel-deck.pdf');

(async () => {
  fs.mkdirSync(OUT_DIR, { recursive: true });

  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: SLIDE_W, height: SLIDE_H, deviceScaleFactor: 2 });
  await page.goto(`file://${HTML_PATH}`, { waitUntil: 'networkidle0' });

  // Wait for fonts
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 800));

  const slideCount = await page.evaluate(() =>
    document.querySelectorAll('.slide').length
  );
  console.log(`Found ${slideCount} slides`);

  const pngPaths = [];

  for (let i = 0; i < slideCount; i++) {
    await page.evaluate((idx) => {
      const slides = document.querySelectorAll('.slide');
      slides.forEach((s, j) => {
        s.style.display = j === idx ? 'grid' : 'none';
      });
    }, i);

    await new Promise(r => setTimeout(r, 120));

    const label = await page.evaluate((idx) => {
      const el = document.querySelectorAll('.slide')[idx];
      return el.dataset.screenLabel || String(idx + 1).padStart(2, '0');
    }, i);

    const safeName = label.replace(/[^a-z0-9]/gi, '-').toLowerCase();
    const pngPath = path.join(OUT_DIR, `slide-${String(i + 1).padStart(2, '0')}-${safeName}.png`);

    await page.screenshot({ path: pngPath, type: 'png' });
    pngPaths.push(pngPath);
    console.log(`  ✓ ${label}`);
  }

  await browser.close();

  // Combine PNGs into PDF using Puppeteer's own PDF engine
  const browser2 = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
  const page2 = await browser2.newPage();

  const imgTags = pngPaths.map(p =>
    `<img src="file://${p}" style="width:100%;height:100%;display:block;page-break-after:always;">`
  ).join('\n');

  await page2.setContent(`
    <html><head><style>
      * { margin:0; padding:0; box-sizing:border-box; }
      body { background:#000; }
      img { width:1920px; height:1080px; display:block; }
    </style></head><body>${imgTags}</body></html>
  `);

  await page2.pdf({
    path: PDF_OUT,
    width: `${SLIDE_W}px`,
    height: `${SLIDE_H}px`,
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
  });

  await browser2.close();

  console.log(`\nPDF saved → ${PDF_OUT}`);
})();
