#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 48px;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 6px; max-width: 1700px; font-size: 56px; line-height: 1.08;">D2C now. Clinic in parallel. Employer at scale.</h1>
    <p class="bm5-sub">One product. Two layers. Three buyers &mdash; each channel earns the next.</p>

    <div class="bm5-svgwrap">
      <svg viewBox="0 0 1900 560" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMid meet">

        <!-- Phase markers -->
        <line x1="605" y1="36" x2="605" y2="452" stroke="rgba(149,74,45,0.22)" stroke-width="1.5" stroke-dasharray="6 4"/>
        <line x1="1130" y1="36" x2="1130" y2="452" stroke="rgba(149,74,45,0.30)" stroke-width="1.5" stroke-dasharray="6 4"/>
        <text x="605" y="22" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 9</text>
        <text x="605" y="34" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">PAID PILOTS</text>
        <text x="1130" y="22" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 18</text>
        <text x="1130" y="34" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">POST-SEED</text>

        <!-- D2C stream — deep terracotta, dominant -->
        <path d="M 80,132 C 210,130 330,122 430,117 C 505,112 545,102 605,95 C 670,85 715,74 780,70 C 905,50 995,30 1130,22 C 1235,17 1350,15 1480,15 L 1480,140 L 80,140 Z" fill="#7D3820" opacity="0.96"/>

        <!-- Clinic stream — rich warm tan, clearly present -->
        <path d="M 80,241 C 200,241 325,241 430,240 C 500,239 545,238 605,236 C 670,230 715,227 780,225 C 905,212 995,203 1130,200 C 1260,198 1370,196 1480,196 L 1480,245 L 80,245 Z" fill="#8B5520" opacity="0.88"/>

        <!-- Employer ghost line -->
        <line x1="80" y1="369" x2="1130" y2="369" stroke="rgba(149,74,45,0.38)" stroke-width="2" stroke-dasharray="8 5"/>

        <!-- Employer stream — lighter terracotta, visible presence -->
        <path d="M 1130,367 C 1210,366 1260,363 1305,362 C 1370,360 1425,358 1480,357 L 1480,370 L 1130,370 Z" fill="#BF7030" opacity="0.82"/>

        <!-- Left channel labels — same weight as right callouts -->
        <text x="110" y="74" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="13" font-weight="700" letter-spacing="3" fill="#7D3820">D2C</text>
        <text x="110" y="197" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="13" font-weight="700" letter-spacing="3" fill="#8B5520">CLINIC</text>
        <text x="110" y="312" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="13" font-weight="700" letter-spacing="3" fill="#BF7030">EMPLOYER</text>

        <!-- Terminal dots at stream right-edge midpoints -->
        <circle cx="1480" cy="78"  r="5" fill="#7D3820" opacity="0.92"/>
        <circle cx="1480" cy="221" r="5" fill="#8B5520" opacity="0.88"/>
        <circle cx="1480" cy="364" r="4" fill="#BF7030" opacity="0.82"/>

        <!-- Connector lines: dot to annotation -->
        <line x1="1485" y1="78"  x2="1516" y2="78"  stroke="#7D3820" stroke-width="1.5" opacity="0.35"/>
        <line x1="1485" y1="221" x2="1516" y2="221" stroke="#8B5520" stroke-width="1.5" opacity="0.35"/>
        <line x1="1485" y1="364" x2="1516" y2="364" stroke="#BF7030" stroke-width="1.5" opacity="0.35"/>

        <!-- X-axis -->
        <line x1="80" y1="452" x2="1480" y2="452" stroke="rgba(149,74,45,0.18)" stroke-width="1"/>

        <!-- Ticks -->
        <line x1="80"   y1="448" x2="80"   y2="456" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="430"  y1="448" x2="430"  y2="456" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="605"  y1="448" x2="605"  y2="456" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="780"  y1="448" x2="780"  y2="456" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="1130" y1="448" x2="1130" y2="456" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="1480" y1="448" x2="1480" y2="456" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>

        <!-- Month labels -->
        <text x="80"   y="476" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 0</text>
        <text x="430"  y="476" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 6</text>
        <text x="605"  y="476" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 9</text>
        <text x="780"  y="476" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 12</text>
        <text x="1130" y="476" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 18</text>
        <text x="1480" y="476" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 24+</text>

        <!-- Annotation rail separator -->
        <line x1="1502" y1="0" x2="1502" y2="452" stroke="rgba(149,74,45,0.10)" stroke-width="1"/>

        <!-- D2C annotation — above/below connector at y=78 -->
        <text x="1518" y="70" font-family="Instrument Serif, serif" font-size="30" fill="#7D3820">$360K&#x2013;$600K ARR</text>
        <text x="1518" y="94" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(125,56,32,0.60)">1,500&#x2013;2,500 SUBSCRIBERS</text>

        <!-- Clinic annotation — above/below connector at y=221 -->
        <text x="1518" y="213" font-family="Instrument Serif, serif" font-size="30" fill="#8B5520">~$70K ARR</text>
        <text x="1518" y="237" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(139,85,32,0.60)">2&#x2013;3 CLINIC PARTNERS</text>

        <!-- Employer annotation — above/below connector at y=364 -->
        <text x="1518" y="356" font-family="Instrument Serif, serif" font-size="26" fill="#BF7030" opacity="0.88">Seed-funded scale</text>
        <text x="1518" y="378" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(191,112,48,0.58)">$10 PEPM &#xB7; 1&#x2013;2 PILOTS</text>

      </svg>
    </div>

    <div class="bm5-cols">
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch1">D2C &mdash; $20/month &middot; Patients buy now</p>
        <p class="bm5-body">Convert WhatsApp beta to paid. Ship Maeve AI, community &amp; education library. Founder-led growth.</p>
        <p class="bm5-proof">WhatsApp beta live. LinkedIn audience: 11K &rarr; 25K.</p>
      </div>
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch2">Clinic SaaS &mdash; $35&ndash;50K ACV &middot; D2C data as proof</p>
        <p class="bm5-body">2&ndash;3 design partners from day one. Paid pilots at Mo. 9 using D2C engagement data.</p>
        <p class="bm5-proof">Clinic cycles are 6&ndash;9 months. Relationships start now, revenue follows.</p>
      </div>
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch3">Employer Benefits &mdash; $10 PEPM &middot; Post-seed scale</p>
        <p class="bm5-body">First conversations at Mo. 12+. Close via Mercer &amp; Gallagher. Distinct from Maven/Carrot.</p>
        <p class="bm5-proof">D2C usage data + clinic logos = the enterprise pitch.</p>
      </div>
    </div>

    <div class="bm5-mktstrip">
      <p class="bm5-mktline">Addressable market: ~400K U.S. fertility patients annually &middot; ~10% blended penetration &middot; ~$300/patient/year = <strong>$12M ARR opportunity</strong>.</p>
      <p class="bm5-mktline">Pre-seed milestone: $500K+ ARR run-rate by seed round.</p>
    </div>
    <p class="bm5-src">U.S. patient volume: SART 2023 &middot; Pricing: women&rsquo;s health and digital health subscription benchmarks</p>

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 6px 0 !important; font-size: 56px !important; }

    .bm5-sub { font-family: 'Instrument Serif', serif; font-style: italic; font-size: 22px; color: var(--ink-soft); margin: 0 0 10px; line-height: 1.3; }

    .bm5-svgwrap { width: 100%; margin-bottom: 8px; }
    .bm5-svgwrap svg { width: 100%; height: auto; display: block; }

    .bm5-cols { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0; margin-bottom: 8px; }
    .bm5-col { padding: 0 28px 0 0; border-right: 1px solid rgba(149,74,45,0.14); }
    .bm5-col:last-child { border-right: none; padding-right: 0; }
    .bm5-col:not(:first-child) { padding-left: 28px; }

    .bm5-ch { font-family: 'Inter Tight', sans-serif; font-size: 13px; font-weight: 700; letter-spacing: 0.10em; text-transform: uppercase; margin: 0 0 7px; line-height: 1.35; }
    .bm5-ch1 { color: #7D3820; }
    .bm5-ch2 { color: #8B5520; }
    .bm5-ch3 { color: #BF7030; }

    .bm5-body { font-family: 'Inter Tight', sans-serif; font-size: 16px; font-weight: 300; color: var(--ink-soft); margin: 0 0 7px; line-height: 1.55; }
    .bm5-proof { font-family: 'Instrument Serif', serif; font-style: italic; font-size: 15px; color: var(--ink-mute); margin: 0; line-height: 1.45; }

    .bm5-mktstrip { border-top: 1.5px solid rgba(149,74,45,0.18); padding-top: 12px; margin-bottom: 6px; }
    .bm5-mktline { font-family: 'Inter Tight', sans-serif; font-size: 16px; font-weight: 400; color: var(--ink-soft); margin: 0 0 3px; line-height: 1.5; }
    .bm5-mktline strong { color: var(--accent); font-weight: 700; }

    .bm5-src { font-family: 'Inter Tight', sans-serif; font-size: 11px; font-style: italic; letter-spacing: 0.04em; color: var(--ink-mute); margin: 0; }
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
