#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 64px; display: flex; flex-direction: column;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 20px; max-width: 1700px; font-size: 52px; line-height: 1.1;">Carousel pairs a patient app with a clinic platform,<br>sold to patients now, clinics in parallel, and employers at scale.</h1>

    <div class="bm6-main">

      <!-- STACKED AREA CHART — left 64% -->
      <div class="bm6-chart">
        <svg viewBox="0 0 1900 680" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMid meet">

          <!-- Phase markers -->
          <line x1="725"  y1="44" x2="725"  y2="540" stroke="rgba(149,74,45,0.20)" stroke-width="1.5" stroke-dasharray="6 4"/>
          <line x1="1370" y1="44" x2="1370" y2="540" stroke="rgba(149,74,45,0.28)" stroke-width="1.5" stroke-dasharray="6 4"/>
          <text x="725"  y="28" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 9</text>
          <text x="725"  y="40" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">PAID PILOTS</text>
          <text x="1370" y="28" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 18</text>
          <text x="1370" y="40" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">POST-SEED</text>

          <!-- D2C fill (bottom layer — the foundation) -->
          <path d="M 80,540 L 80,539 C 290,539 410,531 510,526 C 615,521 672,513 725,505 C 830,495 884,484 940,475 C 1082,453 1231,422 1370,395 C 1547,368 1687,333 1800,305 L 1800,540 Z" fill="#7D3820" opacity="0.93"/>

          <!-- Clinic fill (stacks on D2C, starts growing at Mo.9) -->
          <path d="M 80,539 C 290,539 410,531 510,526 C 615,521 672,513 725,505 C 824,494 877,453 940,420 C 1083,371 1232,332 1370,308 C 1547,283 1687,234 1800,195 L 1800,305 C 1687,333 1547,368 1370,395 C 1231,422 1082,453 940,475 C 884,484 830,495 725,505 C 672,513 615,521 510,526 C 410,531 290,539 80,539 Z" fill="#8B5520" opacity="0.85"/>

          <!-- Employer fill (wedge from Mo.18) -->
          <path d="M 1370,308 C 1547,284 1687,193 1800,150 L 1800,195 C 1687,234 1547,283 1370,308 Z" fill="#BF7030" opacity="0.80"/>

          <!-- X-axis -->
          <line x1="80" y1="540" x2="1800" y2="540" stroke="rgba(149,74,45,0.18)" stroke-width="1"/>

          <!-- Ticks — every 6 months only -->
          <line x1="80"   y1="536" x2="80"   y2="544" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="510"  y1="536" x2="510"  y2="544" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="940"  y1="536" x2="940"  y2="544" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="1370" y1="536" x2="1370" y2="544" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="1800" y1="536" x2="1800" y2="544" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>

          <!-- Month labels — every 6 months -->
          <text x="80"   y="560" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 0</text>
          <text x="510"  y="560" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 6</text>
          <text x="940"  y="560" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 12</text>
          <text x="1370" y="560" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 18</text>
          <text x="1800" y="560" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 24</text>

          <!-- Color legend -->
          <rect x="80"  y="590" width="12" height="12" rx="2" fill="#7D3820" opacity="0.90"/>
          <text x="98"  y="601" font-family="Inter Tight, sans-serif" font-size="13" font-weight="600" letter-spacing="1" fill="rgba(74,56,42,0.60)">D2C</text>
          <rect x="168" y="590" width="12" height="12" rx="2" fill="#8B5520" opacity="0.85"/>
          <text x="186" y="601" font-family="Inter Tight, sans-serif" font-size="13" font-weight="600" letter-spacing="1" fill="rgba(74,56,42,0.60)">Clinic</text>
          <rect x="268" y="590" width="12" height="12" rx="2" fill="#BF7030" opacity="0.80"/>
          <text x="286" y="601" font-family="Inter Tight, sans-serif" font-size="13" font-weight="600" letter-spacing="1" fill="rgba(74,56,42,0.60)">Employer</text>

        </svg>
      </div><!-- /bm6-chart -->

      <!-- RIGHT PANEL — ARR / Milestone / Assumption -->
      <div class="bm6-rpanel">

        <div class="bm6-rp-hd">
          <span></span>
          <span class="bm6-rp-col-lbl">ARR at seed</span>
          <span class="bm6-rp-col-lbl">Milestone &middot; Assumption</span>
        </div>

        <div class="bm6-rp-row" style="border-left: 3px solid #7D3820;">
          <div class="bm6-rp-chan" style="color:#7D3820;">D2C</div>
          <div class="bm6-rp-arr" style="color:#7D3820;">$180K&ndash;<br>$360K</div>
          <div class="bm6-rp-detail">
            <p class="bm6-rp-ms">1,500&ndash;2,500 subscribers paying</p>
            <p class="bm6-rp-as">$20/month subscription</p>
          </div>
        </div>

        <div class="bm6-rp-row" style="border-left: 3px solid #8B5520;">
          <div class="bm6-rp-chan" style="color:#8B5520;">Clinic</div>
          <div class="bm6-rp-arr" style="color:#8B5520;">~$70K</div>
          <div class="bm6-rp-detail">
            <p class="bm6-rp-ms">2&ndash;3 paid pilots signed by Mo. 9</p>
            <p class="bm6-rp-as">$35&ndash;50K ACV</p>
          </div>
        </div>

        <div class="bm6-rp-row" style="border-left: 3px solid #BF7030;">
          <div class="bm6-rp-chan" style="color:#BF7030;">Employer</div>
          <div class="bm6-rp-arr" style="color:#BF7030;">Post-<br>seed</div>
          <div class="bm6-rp-detail">
            <p class="bm6-rp-ms">1&ndash;2 pilots after seed close</p>
            <p class="bm6-rp-as">$10 PEPM &middot; distinct from Maven, Carrot</p>
          </div>
        </div>

      </div><!-- /bm6-rpanel -->

    </div><!-- /bm6-main -->

    <div class="bm6-mktstrip">
      <p class="bm6-mktline">Addressable market: ~400K U.S. fertility patients annually &middot; ~10% blended penetration &middot; ~$200&ndash;$250/patient/year = <strong>~$9M ARR opportunity</strong>.</p>
      <p class="bm6-mktline">Pre-seed milestone: $500K+ ARR run-rate by seed round.</p>
    </div>
    <p class="bm6-src">U.S. patient volume: SART 2023 &middot; Pricing: women&rsquo;s health and digital health subscription benchmarks</p>

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    [data-screen-label="09 Business model"] .frame { display: flex; flex-direction: column; }
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 20px 0 !important; font-size: 52px !important; }

    /* Main two-column layout */
    .bm6-main { display: flex; gap: 40px; align-items: flex-start; margin-bottom: 14px; }
    .bm6-chart { flex: 0 0 63%; }
    .bm6-chart svg { width: 100%; height: auto; display: block; }

    /* Right panel */
    .bm6-rpanel { flex: 1; display: flex; flex-direction: column; padding-top: 44px; }
    .bm6-rp-hd { display: grid; grid-template-columns: 68px 72px 1fr; gap: 10px; padding-bottom: 8px; border-bottom: 1.5px solid rgba(149,74,45,0.18); margin-bottom: 0; }
    .bm6-rp-col-lbl { font-family: 'Inter Tight', sans-serif; font-size: 10px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(74,56,42,0.38); }
    .bm6-rp-row { display: grid; grid-template-columns: 68px 72px 1fr; gap: 10px; padding: 14px 0 14px 12px; border-bottom: 1px solid rgba(149,74,45,0.10); align-items: start; }
    .bm6-rp-chan { font-family: 'Inter Tight', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 0.10em; text-transform: uppercase; padding-top: 4px; }
    .bm6-rp-arr { font-family: 'Instrument Serif', serif; font-size: 22px; line-height: 1.15; }
    .bm6-rp-detail { display: flex; flex-direction: column; gap: 5px; }
    .bm6-rp-ms { font-family: 'Inter Tight', sans-serif; font-size: 15px; font-weight: 400; color: var(--ink); margin: 0; line-height: 1.4; }
    .bm6-rp-as { font-family: 'Inter Tight', sans-serif; font-size: 13px; font-weight: 300; color: var(--ink-mute); margin: 0; line-height: 1.4; }

    /* Bottom strip */
    .bm6-mktstrip { border-top: 1.5px solid rgba(149,74,45,0.18); padding-top: 10px; margin-bottom: 5px; }
    .bm6-mktline { font-family: 'Inter Tight', sans-serif; font-size: 15px; font-weight: 400; color: var(--ink-soft); margin: 0 0 2px; line-height: 1.5; }
    .bm6-mktline strong { color: var(--accent); font-weight: 700; }
    .bm6-src { font-family: 'Inter Tight', sans-serif; font-size: 11px; font-style: italic; letter-spacing: 0.04em; color: var(--ink-mute); margin: 0; }
  </style>
</section>"""

start_marker = '<section class="slide" data-screen-label="09 Business model">'
end_marker = '</section>\n<!-- 9. TRACTION -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)
if start_idx == -1 or end_idx == -1:
    print(f"ERROR: start={start_idx}, end={end_idx}"); exit(1)
end_idx += len('</section>')

new_content = content[:start_idx] + new_slide + content[end_idx:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Done. Replaced {end_idx-start_idx} chars with {len(new_slide)} chars.")
