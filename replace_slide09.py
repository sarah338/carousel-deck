#!/usr/bin/env python3
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = '''<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 48px;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 6px; max-width: 1700px; font-size: 56px; line-height: 1.08;">D2C now. Clinic in parallel. Employer at scale.</h1>
    <p class="bm5-sub">One product. Two layers. Three buyers &mdash; each channel earns the next.</p>

    <!-- REVENUE STREAMS SVG -->
    <div class="bm5-svgwrap">
      <svg viewBox="0 0 1900 460" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMinYMid meet">

        <!-- Vertical phase markers -->
        <line x1="605" y1="36" x2="605" y2="378" stroke="rgba(149,74,45,0.20)" stroke-width="1.5" stroke-dasharray="6 4"/>
        <line x1="1130" y1="36" x2="1130" y2="378" stroke="rgba(149,74,45,0.28)" stroke-width="1.5" stroke-dasharray="6 4"/>

        <!-- Phase marker labels -->
        <text x="605" y="22" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 9</text>
        <text x="605" y="34" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">PAID PILOTS</text>
        <text x="1130" y="22" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.55)">MO. 18</text>
        <text x="1130" y="34" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="10" letter-spacing="2" fill="rgba(149,74,45,0.42)">POST-SEED</text>

        <!-- D2C stream -->
        <path d="M 80,132 C 210,130 330,122 430,117 C 505,112 545,102 605,95 C 670,85 715,74 780,70 C 905,50 995,30 1130,22 C 1235,17 1350,15 1480,15 L 1480,140 L 80,140 Z" fill="#954A2D" opacity="0.82"/>

        <!-- Clinic stream -->
        <path d="M 80,241 C 200,241 325,241 430,240 C 500,239 545,238 605,236 C 670,230 715,227 780,225 C 905,212 995,203 1130,200 C 1260,198 1370,196 1480,196 L 1480,245 L 80,245 Z" fill="#A06432" opacity="0.72"/>

        <!-- Employer ghost (pre-Mo.18) -->
        <line x1="80" y1="369" x2="1130" y2="369" stroke="rgba(149,74,45,0.18)" stroke-width="2" stroke-dasharray="8 5"/>

        <!-- Employer stream (Mo.18+) -->
        <path d="M 1130,367 C 1210,366 1260,363 1305,362 C 1370,360 1425,358 1480,357 L 1480,370 L 1130,370 Z" fill="rgba(149,74,45,0.52)"/>

        <!-- Left channel labels -->
        <text x="72" y="74" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="#954A2D">D2C</text>
        <text x="72" y="197" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="#A06432">CLINIC</text>
        <text x="72" y="312" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.52)">EMPLOYER</text>

        <!-- X-axis baseline -->
        <line x1="80" y1="378" x2="1480" y2="378" stroke="rgba(149,74,45,0.18)" stroke-width="1"/>

        <!-- Axis ticks -->
        <line x1="80"   y1="374" x2="80"   y2="382" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="430"  y1="374" x2="430"  y2="382" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="605"  y1="374" x2="605"  y2="382" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="780"  y1="374" x2="780"  y2="382" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="1130" y1="374" x2="1130" y2="382" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>
        <line x1="1480" y1="374" x2="1480" y2="382" stroke="rgba(149,74,45,0.28)" stroke-width="1.5"/>

        <!-- Month labels -->
        <text x="80"   y="402" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 0</text>
        <text x="430"  y="402" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 6</text>
        <text x="605"  y="402" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 9</text>
        <text x="780"  y="402" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 12</text>
        <text x="1130" y="402" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 18</text>
        <text x="1480" y="402" text-anchor="middle" font-family="Inter Tight, sans-serif" font-size="11" letter-spacing="1" fill="rgba(74,56,42,0.48)">Mo. 24+</text>

        <!-- Separator before annotation rail -->
        <line x1="1502" y1="0" x2="1502" y2="378" stroke="rgba(149,74,45,0.10)" stroke-width="1"/>

        <!-- D2C annotation -->
        <text x="1518" y="58" font-family="Instrument Serif, serif" font-size="30" fill="#954A2D">$360K&#x2013;$600K ARR</text>
        <text x="1518" y="80" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(149,74,45,0.58)">1,500&#x2013;2,500 SUBSCRIBERS</text>

        <!-- Clinic annotation -->
        <text x="1518" y="208" font-family="Instrument Serif, serif" font-size="30" fill="#A06432">~$70K ARR</text>
        <text x="1518" y="230" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(160,100,50,0.58)">2&#x2013;3 CLINIC PARTNERS</text>

        <!-- Employer annotation -->
        <text x="1518" y="352" font-family="Instrument Serif, serif" font-size="26" fill="rgba(149,74,45,0.62)">Seed-funded scale</text>
        <text x="1518" y="372" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(149,74,45,0.44)">$10 PEPM &#xB7; 1&#x2013;2 PILOTS</text>

      </svg>
    </div>

    <!-- THREE TEXT BLOCKS -->
    <div class="bm5-cols">
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch1">D2C &mdash; $20 / month</p>
        <p class="bm5-body">Convert WhatsApp beta to paid. Ship Maeve AI, community &amp; education library. Founder-led growth.</p>
        <p class="bm5-why">Patients buy now; no intermediary needed.</p>
      </div>
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch2">Clinic SaaS &mdash; $35&ndash;50K ACV</p>
        <p class="bm5-body">2&ndash;3 design partners from day one. Convert to paid pilots at Mo. 9 using D2C proof.</p>
        <p class="bm5-why">D2C data becomes the clinic sales tool.</p>
      </div>
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch3">Employer Benefits &mdash; $10 PEPM</p>
        <p class="bm5-body">First conversations at Mo. 12. Close via Mercer &amp; Gallagher post-seed.</p>
        <p class="bm5-why">Clinic proof becomes the enterprise pitch.</p>
      </div>
    </div>

    <!-- FOOTER -->
    <p class="bm5-foot"><em>~400K U.S. fertility patients annually &middot; 10% blended penetration &middot; $300/patient/year = $12M ARR opportunity &middot; Pre-seed milestone: $500K+ ARR run-rate by seed round.</em></p>
    <p class="bm5-src">U.S. patient volume: SART 2023 &middot; Pricing: women&rsquo;s health and digital health subscription benchmarks</p>

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    /* Slide 09 Business Model v5 &#x2014; Revenue Streams */
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 6px 0 !important; font-size: 56px !important; }

    .bm5-sub {
      font-family: \'Instrument Serif\', serif; font-style: italic;
      font-size: 22px; color: var(--ink-soft); margin: 0 0 14px; line-height: 1.3;
    }

    .bm5-svgwrap { width: 100%; margin-bottom: 10px; }
    .bm5-svgwrap svg { width: 100%; height: auto; display: block; }

    .bm5-cols {
      display: grid; grid-template-columns: 1fr 1fr 1fr;
      gap: 0; margin-bottom: 10px;
    }
    .bm5-col {
      padding: 0 32px 0 0;
      border-right: 1px solid rgba(149,74,45,0.12);
    }
    .bm5-col:last-child { border-right: none; padding-right: 0; }
    .bm5-col:not(:first-child) { padding-left: 32px; }

    .bm5-ch {
      font-family: \'Inter Tight\', sans-serif; font-size: 12px; font-weight: 700;
      letter-spacing: 0.14em; text-transform: uppercase; margin: 0 0 5px;
    }
    .bm5-ch1 { color: #954A2D; }
    .bm5-ch2 { color: #A06432; }
    .bm5-ch3 { color: rgba(149,74,45,0.58); }

    .bm5-body {
      font-family: \'Inter Tight\', sans-serif; font-size: 14px; font-weight: 300;
      color: var(--ink-soft); margin: 0 0 5px; line-height: 1.5;
    }
    .bm5-why {
      font-family: \'Instrument Serif\', serif; font-style: italic;
      font-size: 15px; color: var(--ink-mute); margin: 0; line-height: 1.4;
    }

    .bm5-foot {
      font-family: \'Instrument Serif\', serif; font-size: 16px;
      color: var(--ink-soft); margin: 0 0 4px; line-height: 1.5;
    }
    .bm5-src {
      font-family: \'Inter Tight\', sans-serif; font-size: 11px; font-style: italic;
      letter-spacing: 0.04em; color: var(--ink-mute); margin: 0;
    }
  </style>
</section>'''

# Find section boundaries
start_marker = '<section class="slide" data-screen-label="09 Business model">'
end_marker = '</section>\n<!-- 9. TRACTION -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: start={start_idx}, end={end_idx}")
    exit(1)

end_idx += len('</section>')

new_content = content[:start_idx] + new_slide + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Replaced slide 09 (chars {start_idx}–{end_idx})")
print(f"Old length: {end_idx - start_idx}, New length: {len(new_slide)}")
