#!/usr/bin/env node
// Uses the deck's built-in print mode to export a pixel-perfect PDF.
const puppeteer = require('puppeteer');
const path = require('path');

const W = 1920;
const H = 1080;
const HTML = `file://${path.join(__dirname, 'index.html')}`;
const OUT  = path.join(__dirname, 'carousel-deck.pdf');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--font-render-hinting=none'],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 2 });
  await page.goto(HTML, { waitUntil: 'networkidle0' });

  // Wait for web fonts
  await page.evaluateHandle('document.fonts.ready');
  await new Promise(r => setTimeout(r, 1200));

  // Activate the deck's own print layout
  await page.evaluate(() => {
    const stage = document.querySelector('deck-stage');
    if (stage) stage.style.cssText =
      'display:block;position:static;width:1920px;height:auto;overflow:visible;transform:none;';
    document.querySelectorAll('section.slide').forEach(s => {
      s.style.cssText =
        'position:relative!important;display:block!important;' +
        'width:1920px!important;height:1080px!important;' +
        'transform:none!important;break-after:page!important;overflow:hidden!important;';
    });
  });

  await new Promise(r => setTimeout(r, 400));

  await page.pdf({
    path: OUT,
    width:  `${W}px`,
    height: `${H}px`,
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 },
  });

  await browser.close();
  const { statSync } = require('fs');
  const mb = (statSync(OUT).size / 1024 / 1024).toFixed(1);
  console.log(`✓ carousel-deck.pdf  (${mb} MB)  →  ${OUT}`);
})();
