#!/usr/bin/env node
// Uses deck-stage's own goTo() API to navigate each slide,
// proxies Google Fonts through Node, screenshots, combines into PDF.
const puppeteer  = require('puppeteer');
const { PDFDocument } = require('pdf-lib');
const path  = require('path');
const fs    = require('fs');

const W    = 1920;
const H    = 1080;
const HTML = `file://${path.join(__dirname, 'index.html')}`;
const OUT  = path.join(__dirname, 'carousel-deck.pdf');

// Pre-built CSS with all fonts embedded as base64 data URIs
const EMBEDDED_FONT_CSS = fs.readFileSync(path.join(__dirname, 'fonts', 'embedded-fonts.css'));

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none'],
  });

  const page = await browser.newPage();
  // Match the deck's design size exactly so scale = 1.0
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 2 });

  // Serve embedded fonts — no network calls needed
  await page.setRequestInterception(true);
  page.on('request', req => {
    const u = req.url();
    if (u.includes('fonts.googleapis.com')) {
      // Return pre-built CSS with data URIs instead of hitting the network
      req.respond({ status: 200, contentType: 'text/css; charset=utf-8', body: EMBEDDED_FONT_CSS });
    } else if (u.includes('fonts.gstatic.com')) {
      // All font data is already embedded in the CSS above
      req.abort();
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

  // Hide the nav overlay permanently before capturing
  await page.evaluate(() => {
    const stage = document.querySelector('deck-stage');
    const overlay = stage.shadowRoot?.querySelector('.overlay');
    if (overlay) {
      overlay.removeAttribute('data-visible');
      overlay.style.cssText = 'display:none!important;';
    }
  });

  const pngs = [];
  for (let i = 0; i < slideCount; i++) {
    await page.evaluate((idx) => {
      const stage = document.querySelector('deck-stage');
      stage.goTo(idx);
      // Re-suppress overlay after each navigation
      const overlay = stage.shadowRoot?.querySelector('.overlay');
      if (overlay) overlay.style.cssText = 'display:none!important;';
    }, i);
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
