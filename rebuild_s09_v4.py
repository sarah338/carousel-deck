#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 72px; display: flex; flex-direction: column;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 24px; max-width: 1700px; font-size: 52px; line-height: 1.1;">Carousel pairs a patient app with a clinic platform,<br>sold to patients now, clinics in parallel, and employers at scale.</h1>

    <div class="bm7-main">

      <!-- STREAMS CHART -->
      <div class="bm7-chart">
        <!-- negative x origin gives labels room on the left; no clipping -->
        <svg viewBox="-100 0 1360 600" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMid meet">

          <!-- Phase markers — subtle dashes, small labels -->
          <line x1="480" y1="50" x2="480" y2="450" stroke="rgba(149,74,45,0.20)" stroke-width="1.5" stroke-dasharray="6 4"/>
          <line x1="900" y1="50" x2="900" y2="450" stroke="rgba(149,74,45,0.26)" stroke-width="1.5" stroke-dasharray="6 4"/>
          <text x="480" y="38" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="500" letter-spacing="2" fill="rgba(149,74,45,0.50)">MO. 9</text>
          <text x="900" y="38" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="500" letter-spacing="2" fill="rgba(149,74,45,0.50)">MO. 18</text>

          <!-- D2C stream — flat early, ramps after Mo.9 -->
          <path d="M 60,140 C 160,140 300,140 360,138 C 420,136 455,124 480,112 C 540,98 580,82 640,72 C 760,52 860,38 900,33 C 980,24 1080,18 1200,14 L 1200,140 L 60,140 Z" fill="#7D3820" opacity="0.93"/>

          <!-- Clinic stream — flat until Mo.9, then grows -->
          <path d="M 60,248 C 180,248 320,248 360,247 C 430,246 460,245 480,243 C 540,236 580,228 640,220 C 760,206 860,196 900,192 C 980,186 1080,180 1200,176 L 1200,252 L 60,252 Z" fill="#8B5520" opacity="0.88"/>

          <!-- Employer ghost line -->
          <line x1="60" y1="368" x2="900" y2="368" stroke="rgba(149,74,45,0.32)" stroke-width="1.5" stroke-dasharray="8 5"/>

          <!-- Employer stream — emerges at Mo.18 -->
          <path d="M 900,366 C 980,364 1060,360 1120,357 C 1160,355 1185,352 1200,350 L 1200,370 L 900,370 Z" fill="#BF7030" opacity="0.82"/>

          <!-- Stream labels — left of chart, text-anchor end, negative x safe -->
          <text x="48" y="80"  text-anchor="end" font-family="Inter Tight, sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#7D3820">D2C</text>
          <text x="48" y="206" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#8B5520">CLINIC</text>
          <text x="48" y="310" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="12" font-weight="700" letter-spacing="3" fill="#BF7030">EMPLOYER</text>

          <!-- X-axis -->
          <line x1="60" y1="450" x2="1200" y2="450" stroke="rgba(149,74,45,0.16)" stroke-width="1"/>

          <!-- Ticks — every 6 months -->
          <line x1="60"   y1="446" x2="60"   y2="454" stroke="rgba(149,74,45,0.26)" stroke-width="1.5"/>
          <line x1="340"  y1="446" x2="340"  y2="454" stroke="rgba(149,74,45,0.26)" stroke-width="1.5"/>
          <line x1="620"  y1="446" x2="620"  y2="454" stroke="rgba(149,74,45,0.26)" stroke-width="1.5"/>
          <line x1="900"  y1="446" x2="900"  y2="454" stroke="rgba(149,74,45,0.26)" stroke-width="1.5"/>
          <line x1="1200" y1="446" x2="1200" y2="454" stroke="rgba(149,74,45,0.26)" stroke-width="1.5"/>

          <!-- Month labels -->
          <text x="60"   y="474" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.45)">Mo. 0</text>
          <text x="340"  y="474" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.45)">Mo. 6</text>
          <text x="620"  y="474" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.45)">Mo. 12</text>
          <text x="900"  y="474" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.45)">Mo. 18</text>
          <text x="1200" y="474" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="1" fill="rgba(74,56,42,0.45)">Mo. 24</text>

          <!-- Terminal dots -->
          <circle cx="1200" cy="77"  r="5" fill="#7D3820" opacity="0.90"/>
          <circle cx="1200" cy="214" r="5" fill="#8B5520" opacity="0.86"/>
          <circle cx="1200" cy="360" r="4" fill="#BF7030" opacity="0.80"/>

        </svg>
      </div><!-- /bm7-chart -->

      <!-- RIGHT PANEL — 2-col: channel + metric/milestone -->
      <div class="bm7-rpanel">

        <div class="bm7-rp-row bm7-rp-first" style="border-left: 3px solid #7D3820;">
          <div class="bm7-rp-chan" style="color:#7D3820;">D2C</div>
          <div>
            <p class="bm7-rp-metric" style="color:#7D3820;">$180K &ndash; $360K ARR</p>
            <p class="bm7-rp-ms">1,500 &ndash; 2,500 subscribers paying</p>
          </div>
        </div>

        <div class="bm7-rp-row" style="border-left: 3px solid #8B5520;">
          <div class="bm7-rp-chan" style="color:#8B5520;">Clinic</div>
          <div>
            <p class="bm7-rp-metric" style="color:#8B5520;">~$70K ARR</p>
            <p class="bm7-rp-ms">2 &ndash; 3 paid pilots signed by Mo. 9</p>
          </div>
        </div>

        <div class="bm7-rp-row" style="border-left: 3px solid #BF7030;">
          <div class="bm7-rp-chan" style="color:#BF7030;">Employer</div>
          <div>
            <p class="bm7-rp-metric" style="color:#BF7030;">$10 PEPM</p>
            <p class="bm7-rp-ms">1 &ndash; 2 pilots after seed close</p>
          </div>
        </div>

      </div><!-- /bm7-rpanel -->

    </div><!-- /bm7-main -->

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    [data-screen-label="09 Business model"] .frame { display: flex; flex-direction: column; }
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 24px 0 !important; font-size: 52px !important; }

    .bm7-main { display: flex; gap: 48px; align-items: center; flex: 1; min-height: 0; }
    .bm7-chart { flex: 1; min-width: 0; }
    .bm7-chart svg { width: 100%; height: auto; display: block; }

    .bm7-rpanel { flex: 0 0 300px; display: flex; flex-direction: column; gap: 0; }

    .bm7-rp-row {
      display: grid; grid-template-columns: 60px 1fr; gap: 12px;
      padding: 18px 0 18px 14px;
      border-bottom: 1px solid rgba(149,74,45,0.10);
      align-items: start;
    }
    .bm7-rp-first { border-top: 1.5px solid rgba(149,74,45,0.18); }
    .bm7-rp-chan {
      font-family: 'Inter Tight', sans-serif; font-size: 11px; font-weight: 700;
      letter-spacing: 0.14em; text-transform: uppercase; padding-top: 3px;
    }
    .bm7-rp-metric {
      font-family: 'Instrument Serif', serif; font-size: 24px; line-height: 1.1;
      margin: 0 0 5px;
    }
    .bm7-rp-ms {
      font-family: 'Inter Tight', sans-serif; font-size: 14px; font-weight: 300;
      color: var(--ink-soft); line-height: 1.45; margin: 0;
    }
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
