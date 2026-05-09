#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 72px; display: flex; flex-direction: column;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 20px; max-width: 1700px; font-size: 52px; line-height: 1.1;">Carousel pairs a patient app with a clinic platform,<br>sold to patients now, clinics in parallel, and employers at scale.</h1>

    <div class="bm7-main">

      <!-- STREAMS CHART — left -->
      <div class="bm7-chart">
        <svg viewBox="0 0 1260 540" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMid meet">

          <!-- Phase markers -->
          <line x1="480" y1="36" x2="480" y2="440" stroke="rgba(149,74,45,0.22)" stroke-width="1.5" stroke-dasharray="6 4"/>
          <line x1="900" y1="36" x2="900" y2="440" stroke="rgba(149,74,45,0.30)" stroke-width="1.5" stroke-dasharray="6 4"/>
          <text x="480"  y="22" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="16" font-weight="700" letter-spacing="2" fill="rgba(149,74,45,0.65)">MO. 9</text>
          <text x="900" y="22" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="16" font-weight="700" letter-spacing="2" fill="rgba(149,74,45,0.65)">MO. 18</text>

          <!-- D2C stream — flat early, ramps after Mo.9 -->
          <path d="M 60,130 C 160,130 300,130 360,129 C 420,128 455,118 480,108 C 540,96 580,82 640,74 C 760,56 860,40 900,36 C 980,28 1080,22 1200,18 L 1200,130 L 60,130 Z" fill="#7D3820" opacity="0.93"/>

          <!-- Clinic stream — flat until Mo.9, then grows -->
          <path d="M 60,238 C 180,238 320,238 360,237 C 430,236 460,235 480,233 C 540,226 580,220 640,214 C 760,202 860,192 900,188 C 980,182 1080,176 1200,172 L 1200,242 L 60,242 Z" fill="#8B5520" opacity="0.88"/>

          <!-- Employer ghost line (pre-Mo.18) -->
          <line x1="60" y1="358" x2="900" y2="358" stroke="rgba(149,74,45,0.35)" stroke-width="2" stroke-dasharray="8 5"/>

          <!-- Employer stream — emerges at Mo.18 -->
          <path d="M 900,356 C 980,354 1060,350 1120,347 C 1160,345 1185,342 1200,340 L 1200,360 L 900,360 Z" fill="#BF7030" opacity="0.82"/>

          <!-- Stream labels — left side -->
          <text x="42" y="68"  text-anchor="end" font-family="Inter Tight, sans-serif" font-size="13" font-weight="700" letter-spacing="3" fill="#7D3820">D2C</text>
          <text x="42" y="196" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="13" font-weight="700" letter-spacing="3" fill="#8B5520">CLINIC</text>
          <text x="42" y="302" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="13" font-weight="700" letter-spacing="3" fill="#BF7030">EMPLOYER</text>

          <!-- X-axis -->
          <line x1="60" y1="440" x2="1200" y2="440" stroke="rgba(149,74,45,0.18)" stroke-width="1"/>

          <!-- Ticks — every 6 months -->
          <line x1="60"   y1="436" x2="60"   y2="444" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="340"  y1="436" x2="340"  y2="444" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="620"  y1="436" x2="620"  y2="444" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="900"  y1="436" x2="900"  y2="444" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
          <line x1="1200" y1="436" x2="1200" y2="444" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>

          <!-- Month labels — every 6 months -->
          <text x="60"   y="462" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 0</text>
          <text x="340"  y="462" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 6</text>
          <text x="620"  y="462" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 12</text>
          <text x="900"  y="462" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 18</text>
          <text x="1200" y="462" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="13" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 24</text>

          <!-- Terminal dots -->
          <circle cx="1200" cy="74"  r="5" fill="#7D3820" opacity="0.92"/>
          <circle cx="1200" cy="207" r="5" fill="#8B5520" opacity="0.88"/>
          <circle cx="1200" cy="350" r="4" fill="#BF7030" opacity="0.82"/>

        </svg>
      </div><!-- /bm7-chart -->

      <!-- RIGHT PANEL -->
      <div class="bm7-rpanel">

        <div class="bm7-rp-hd">
          <span></span>
          <span class="bm7-rp-lbl">ARR</span>
          <span class="bm7-rp-lbl">Milestone</span>
        </div>

        <div class="bm7-rp-row" style="border-left: 3px solid #7D3820;">
          <div class="bm7-rp-chan" style="color:#7D3820;">D2C</div>
          <div class="bm7-rp-arr" style="color:#7D3820;">$180K&ndash;<br>$360K</div>
          <div class="bm7-rp-ms">1,500&ndash;2,500 subscribers paying</div>
        </div>

        <div class="bm7-rp-row" style="border-left: 3px solid #8B5520;">
          <div class="bm7-rp-chan" style="color:#8B5520;">Clinic</div>
          <div class="bm7-rp-arr" style="color:#8B5520;">~$70K</div>
          <div class="bm7-rp-ms">2&ndash;3 paid pilots signed by Mo. 9</div>
        </div>

        <div class="bm7-rp-row" style="border-left: 3px solid #BF7030;">
          <div class="bm7-rp-chan" style="color:#BF7030;">Employer</div>
          <div class="bm7-rp-arr" style="color:#BF7030;">Post-seed</div>
          <div class="bm7-rp-ms">1&ndash;2 pilots after seed close &middot; $10 PEPM</div>
        </div>

      </div><!-- /bm7-rpanel -->

    </div><!-- /bm7-main -->

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    [data-screen-label="09 Business model"] .frame { display: flex; flex-direction: column; }
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 20px 0 !important; font-size: 52px !important; }

    .bm7-main { display: flex; gap: 48px; align-items: flex-start; flex: 1; min-height: 0; }
    .bm7-chart { flex: 1; }
    .bm7-chart svg { width: 100%; height: auto; display: block; }

    .bm7-rpanel { flex: 0 0 320px; display: flex; flex-direction: column; padding-top: 36px; }
    .bm7-rp-hd { display: grid; grid-template-columns: 64px 80px 1fr; gap: 10px; padding-bottom: 8px; border-bottom: 1.5px solid rgba(149,74,45,0.18); }
    .bm7-rp-lbl { font-family: 'Inter Tight', sans-serif; font-size: 10px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(74,56,42,0.38); }
    .bm7-rp-row { display: grid; grid-template-columns: 64px 80px 1fr; gap: 10px; padding: 16px 0 16px 12px; border-bottom: 1px solid rgba(149,74,45,0.10); align-items: start; }
    .bm7-rp-chan { font-family: 'Inter Tight', sans-serif; font-size: 12px; font-weight: 700; letter-spacing: 0.10em; text-transform: uppercase; padding-top: 4px; }
    .bm7-rp-arr { font-family: 'Instrument Serif', serif; font-size: 22px; line-height: 1.15; }
    .bm7-rp-ms { font-family: 'Inter Tight', sans-serif; font-size: 14px; font-weight: 300; color: var(--ink-soft); line-height: 1.45; padding-top: 4px; }
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
