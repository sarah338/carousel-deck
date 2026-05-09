#!/usr/bin/env node
// Builds fonts/embedded-fonts.css with base64 data URIs so Puppeteer
// doesn't need network access to fonts.gstatic.com
const https = require('https');
const fs    = require('fs');
const path  = require('path');

const CACHE_DIR = path.join(__dirname, '.font-cache');
const FONTS_DIR = path.join(__dirname, 'fonts');
const OUT       = path.join(FONTS_DIR, 'embedded-fonts.css');

const FONTS_URL = 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@200;300;400;500&display=swap';

function fetchBuffer(url) {
  return new Promise((resolve, reject) => {
    const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36';
    https.get(url, { headers: { 'User-Agent': UA } }, res => {
      if (res.statusCode >= 300 && res.headers.location)
        return fetchBuffer(res.headers.location).then(resolve).catch(reject);
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => resolve(Buffer.concat(chunks)));
      res.on('error', reject);
    }).on('error', reject);
  });
}

function cachedFetch(url) {
  fs.mkdirSync(CACHE_DIR, { recursive: true });
  const key  = Buffer.from(url).toString('base64').replace(/[/+=]/g, '_').slice(-80);
  const file = path.join(CACHE_DIR, key);
  if (fs.existsSync(file)) { console.log(`  cache hit: ${url.split('/').pop()}`); return Promise.resolve(fs.readFileSync(file)); }
  console.log(`  fetching: ${url.split('/').pop()}`);
  return fetchBuffer(url).then(buf => { fs.writeFileSync(file, buf); return buf; });
}

(async () => {
  fs.mkdirSync(FONTS_DIR, { recursive: true });

  console.log('Fetching Google Fonts CSS...');
  const cssBuf = await cachedFetch(FONTS_URL);
  const css    = cssBuf.toString('utf-8');

  // Find all unique woff2 URLs
  const urlSet = new Set([...css.matchAll(/url\((https:\/\/fonts\.gstatic\.com[^)]+)\)/g)].map(m => m[1]));
  console.log(`Found ${urlSet.size} unique font URLs`);

  // Fetch all woff2 files and build replacement map
  const urlToData = {};
  for (const url of urlSet) {
    const buf  = await cachedFetch(url);
    urlToData[url] = `data:font/woff2;base64,${buf.toString('base64')}`;
  }

  // Replace all URLs with data URIs
  let embedded = css;
  for (const [url, dataUri] of Object.entries(urlToData)) {
    embedded = embedded.split(url).join(dataUri);
  }

  fs.writeFileSync(OUT, embedded);
  const kb = (fs.statSync(OUT).size / 1024).toFixed(0);
  console.log(`\nWrote fonts/embedded-fonts.css (${kb} KB)`);
})();
