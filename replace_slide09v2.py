#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 48px;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 6px; max-width: 1700px; font-size: 56px; line-height: 1.08;">D2C now. Clinic in parallel. Employer at scale.</h1>
    <p class="bm6-sub">One product. Two layers. Three buyers &mdash; each channel earns the next.</p>

    <div class="bm6-svgwrap">
      <svg viewBox="0 0 1900 420" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMid meet">

        <!-- Phase markers -->
        <line x1="630" y1="36" x2="630" y2="328" stroke="rgba(149,74,45,0.22)" stroke-width="1.5" stroke-dasharray="6 4"/>
        <line x1="1140" y1="36" x2="1140" y2="328" stroke="rgba(149,74,45,0.30)" stroke-width="1.5" stroke-dasharray="6 4"/>
        <text x="630" y="20" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 9</text>
        <text x="630" y="33" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">PAID PILOTS</text>
        <text x="1140" y="20" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 18</text>
        <text x="1140" y="33" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">POST-SEED</text>

        <!-- D2C area (bottom, largest) -->
        <path fill="#954A2D" opacity="0.84" d="
          M 120,326 C 256,326 324,289 460,289
          C 528,289 562,263 630,263
          C 698,263 732,226 800,226
          C 936,226 1004,160 1140,160
          C 1276,160 1344,83 1480,83
          L 1480,326 Z"/>

        <!-- Clinic area (stacked on D2C) -->
        <path fill="#B07040" opacity="0.70" d="
          M 120,326 C 256,326 324,289 460,289
          C 528,289 562,262 630,262
          C 698,262 732,217 800,217
          C 936,217 1004,139 1140,139
          C 1276,139 1344,46 1480,46
          L 1480,83
          C 1344,83 1276,160 1140,160
          C 1004,160 936,226 800,226
          C 732,226 698,263 630,263
          C 562,263 528,289 460,289
          C 324,289 256,326 120,326 Z"/>

        <!-- Employer wedge (Mo.18 onward, top layer) -->
        <path fill="rgba(200,160,100,0.65)" d="
          M 1140,139 C 1276,139 1344,30 1480,30
          L 1480,46 C 1344,46 1276,139 1140,139 Z"/>

        <!-- X-axis -->
        <line x1="120" y1="328" x2="1480" y2="328" stroke="rgba(149,74,45,0.18)" stroke-width="1"/>

        <!-- Ticks -->
        <line x1="120"  y1="324" x2="120"  y2="332" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="460"  y1="324" x2="460"  y2="332" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="630"  y1="324" x2="630"  y2="332" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="800"  y1="324" x2="800"  y2="332" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="1140" y1="324" x2="1140" y2="332" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="1480" y1="324" x2="1480" y2="332" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>

        <!-- Month labels -->
        <text x="120"  y="349" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 0</text>
        <text x="460"  y="349" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 6</text>
        <text x="630"  y="349" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 9</text>
        <text x="800"  y="349" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 12</text>
        <text x="1140" y="349" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 18</text>
        <text x="1480" y="349" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 24+</text>

        <!-- Y hint -->
        <text x="112" y="330" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="10" fill="rgba(74,56,42,0.30)">$0</text>
        <text x="112" y="164" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="10" fill="rgba(74,56,42,0.22)">~$600K</text>

        <!-- Annotation rail separator -->
        <line x1="1496" y1="36" x2="1496" y2="328" stroke="rgba(149,74,45,0.10)" stroke-width="1"/>

        <!-- Connectors -->
        <line x1="1481" y1="205" x2="1504" y2="205" stroke="#954A2D" stroke-width="1" opacity="0.30"/>
        <line x1="1481" y1="65"  x2="1504" y2="65"  stroke="#A06432" stroke-width="1" opacity="0.30"/>
        <line x1="1481" y1="38"  x2="1504" y2="38"  stroke="rgba(149,74,45,0.5)" stroke-width="1" opacity="0.30"/>

        <!-- D2C annotation -->
        <text x="1508" y="197" font-family="Instrument Serif, serif" font-size="22" fill="#954A2D">$360K&#x2013;$600K ARR</text>
        <text x="1508" y="214" font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="2" fill="rgba(149,74,45,0.55)">1,500&#x2013;2,500 SUBSCRIBERS</text>

        <!-- Clinic annotation -->
        <text x="1508" y="59"  font-family="Instrument Serif, serif" font-size="20" fill="#A06432">~$70K ARR</text>
        <text x="1508" y="75"  font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="2" fill="rgba(160,100,50,0.55)">2&#x2013;3 CLINIC PARTNERS</text>

        <!-- Employer annotation -->
        <text x="1508" y="36"  font-family="Instrument Serif, serif" font-size="14" fill="rgba(149,74,45,0.60)">Seed-funded scale &#xB7; $10 PEPM</text>

      </svg>
    </div>

    <div class="bm6-cols">
      <div class="bm6-col">
        <p class="bm6-ch bm6-ch1">D2C &mdash; $20 / month</p>
        <p class="bm6-body">Convert WhatsApp beta to paid. Ship Maeve AI, community &amp; education library. Founder-led growth.</p>
        <p class="bm6-why">Patients buy now; no intermediary needed.</p>
      </div>
      <div class="bm6-col">
        <p class="bm6-ch bm6-ch2">Clinic SaaS &mdash; $35&ndash;50K ACV</p>
        <p class="bm6-body">2&ndash;3 design partners from day one. Paid pilots at Mo. 9 using D2C proof.</p>
        <p class="bm6-why">D2C data becomes the clinic sales tool.</p>
      </div>
      <div class="bm6-col">
        <p class="bm6-ch bm6-ch3">Employer Benefits &mdash; $10 PEPM</p>
        <p class="bm6-body">First conversations at Mo. 12. Close via Mercer &amp; Gallagher post-seed.</p>
        <p class="bm6-why">Clinic proof becomes the enterprise pitch.</p>
      </div>
    </div>

    <p class="bm6-foot"><em>~400K U.S. fertility patients annually &middot; 10% blended penetration &middot; $300/patient/year = $12M ARR opportunity &middot; Pre-seed milestone: $500K+ ARR run-rate by seed round.</em></p>
    <p class="bm6-src">U.S. patient volume: SART 2023 &middot; Pricing: women&rsquo;s health and digital health subscription benchmarks</p>

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 6px 0 !important; font-size: 56px !important; }
    .bm6-sub { font-family: 'Instrument Serif', serif; font-style: italic; font-size: 22px; color: var(--ink-soft); margin: 0 0 12px; line-height: 1.3; }
    .bm6-svgwrap { width: 100%; margin-bottom: 10px; }
    .bm6-svgwrap svg { width: 100%; height: auto; display: block; }
    .bm6-cols { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0; margin-bottom: 10px; }
    .bm6-col { padding: 0 32px 0 0; border-right: 1px solid rgba(149,74,45,0.12); }
    .bm6-col:last-child { border-right: none; padding-right: 0; }
    .bm6-col:not(:first-child) { padding-left: 32px; }
    .bm6-ch { font-family: 'Inter Tight', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; margin: 0 0 5px; }
    .bm6-ch1 { color: #954A2D; }
    .bm6-ch2 { color: #A06432; }
    .bm6-ch3 { color: rgba(149,74,45,0.58); }
    .bm6-body { font-family: 'Inter Tight', sans-serif; font-size: 14px; font-weight: 300; color: var(--ink-soft); margin: 0 0 5px; line-height: 1.5; }
    .bm6-why { font-family: 'Instrument Serif', serif; font-style: italic; font-size: 15px; color: var(--ink-mute); margin: 0; line-height: 1.4; }
    .bm6-foot { font-family: 'Instrument Serif', serif; font-size: 16px; color: var(--ink-soft); margin: 0 0 4px; line-height: 1.5; }
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
