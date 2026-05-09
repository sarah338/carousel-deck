#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 68px; display: flex; flex-direction: column;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 22px; max-width: 1700px; font-size: 52px; line-height: 1.1;">Carousel pairs a patient app with a clinic platform,<br>sold to patients now, clinics in parallel, and employers at scale.</h1>

    <div class="bm8-rows">

      <!-- D2C -->
      <div class="bm8-row" style="--ch: #7D3820;">
        <div class="bm8-left">
          <span class="bm8-tag">D2C &middot; Patients &middot; Now</span>
          <p class="bm8-price">$20</p>
          <p class="bm8-unit">/ month</p>
        </div>
        <div class="bm8-mid">
          <p class="bm8-strategy">Direct-to-patient subscription. Convert WhatsApp Beta Community to paid. Ship Maeve AI, curated community, milestone tracking, and education library. Founder-led growth on LinkedIn and Instagram.</p>
          <p class="bm8-why"><span class="bm8-why-lbl">Why now.</span> Lowest cost to launch. Generates the engagement data that earns the clinic and employer pitch.</p>
        </div>
        <div class="bm8-right">
          <p class="bm8-ms-fig">1,500&ndash;2,500<br>subscribers</p>
          <p class="bm8-ms-arr">$180K&ndash;$360K ARR &middot; Month 18</p>
        </div>
      </div>

      <!-- Clinic -->
      <div class="bm8-row" style="--ch: #8B5520;">
        <div class="bm8-left">
          <span class="bm8-tag">Clinic &middot; In parallel</span>
          <p class="bm8-price">$35&ndash;50K</p>
          <p class="bm8-unit">/ clinic ACV</p>
        </div>
        <div class="bm8-mid">
          <p class="bm8-strategy">Build 2&ndash;3 design partner clinic relationships from day one. Co-develop the clinic dashboard with REI input. Convert design partners to paid SaaS pilots at Month 9, using D2C engagement data as the proof point.</p>
          <p class="bm8-why"><span class="bm8-why-lbl">Why parallel.</span> Clinic sales cycles are 6&ndash;9 months. Relationships start now; revenue follows.</p>
        </div>
        <div class="bm8-right">
          <p class="bm8-ms-fig">2&ndash;3 paid<br>pilots</p>
          <p class="bm8-ms-arr">~$70&ndash;150K ARR &middot; Month 18</p>
        </div>
      </div>

      <!-- Employer -->
      <div class="bm8-row" style="--ch: #BF7030;">
        <div class="bm8-left">
          <span class="bm8-tag">Employer &middot; At scale</span>
          <p class="bm8-price">$10</p>
          <p class="bm8-unit">per employee / month</p>
        </div>
        <div class="bm8-mid">
          <p class="bm8-strategy">First conversations begin Month 12+. Close through brokers Mercer and Gallagher post-seed. Position distinct from Maven and Carrot &mdash; fertility-specific, longitudinal, integrated with clinic care.</p>
          <p class="bm8-why"><span class="bm8-why-lbl">Why last.</span> Enterprise buyers need both consumer brand and clinical credibility before signing.</p>
        </div>
        <div class="bm8-right">
          <p class="bm8-ms-fig">1&ndash;2 employer<br>pilots</p>
          <p class="bm8-ms-arr">Seed-funded &middot; enterprise scale</p>
        </div>
      </div>

    </div><!-- /bm8-rows -->

    <div class="bm8-footer">
      <p class="bm8-summary">Pre-seed milestone: $500K+ ARR run-rate across all three channels by seed round. Addressable market: ~400K U.S. fertility patients annually &middot; ~10% blended penetration &middot; ~$200&ndash;250/patient/year = ~$8&ndash;10M ARR opportunity.</p>
      <p class="bm8-src">U.S. patient volume: SART 2023 &middot; Pricing: subscription benchmarks across women&rsquo;s health and digital health peer set.</p>
    </div>

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    [data-screen-label="09 Business model"] .frame { display: flex; flex-direction: column; }
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 22px 0 !important; font-size: 52px !important; }

    .bm8-rows {
      display: flex;
      flex-direction: column;
      flex: 1;
      min-height: 0;
      border-top: 1.5px solid rgba(149,74,45,0.18);
      margin-bottom: 14px;
    }

    .bm8-row {
      display: grid;
      grid-template-columns: 230px 1fr 300px;
      gap: 52px;
      flex: 1;
      align-items: center;
      border-bottom: 1px solid rgba(149,74,45,0.12);
    }

    .bm8-left {
      display: flex;
      flex-direction: column;
      border-left: 3px solid var(--ch);
      padding-left: 22px;
    }

    .bm8-tag {
      font-family: 'Inter Tight', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--ch);
      opacity: 0.72;
    }

    .bm8-price {
      font-family: 'Instrument Serif', serif;
      font-size: 64px;
      line-height: 1.0;
      color: var(--ch);
      margin: 8px 0 3px;
    }

    .bm8-unit {
      font-family: 'Inter Tight', sans-serif;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--ch);
      opacity: 0.48;
      margin: 0;
    }

    .bm8-mid {
      display: flex;
      flex-direction: column;
      gap: 11px;
    }

    .bm8-strategy {
      font-family: 'Inter Tight', sans-serif;
      font-size: 17px;
      font-weight: 400;
      line-height: 1.58;
      color: var(--ink);
      margin: 0;
    }

    .bm8-why {
      font-family: 'Inter Tight', sans-serif;
      font-size: 15px;
      font-weight: 300;
      font-style: italic;
      line-height: 1.52;
      color: var(--ink-mute);
      margin: 0;
    }

    .bm8-why-lbl {
      font-style: normal;
      font-weight: 700;
      color: var(--ch);
      letter-spacing: 0.04em;
    }

    .bm8-right {
      text-align: right;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .bm8-ms-fig {
      font-family: 'Instrument Serif', serif;
      font-size: 26px;
      line-height: 1.2;
      color: var(--ch);
      margin: 0;
    }

    .bm8-ms-arr {
      font-family: 'Inter Tight', sans-serif;
      font-size: 14px;
      font-weight: 500;
      letter-spacing: 0.03em;
      color: var(--ch);
      opacity: 0.65;
      margin: 0;
    }

    .bm8-footer {
      border-top: 1.5px solid rgba(149,74,45,0.18);
      padding-top: 10px;
    }

    .bm8-summary {
      font-family: 'Inter Tight', sans-serif;
      font-size: 14px;
      font-weight: 400;
      font-style: italic;
      color: var(--ink-soft);
      margin: 0 0 4px;
      line-height: 1.52;
    }

    .bm8-src {
      font-family: 'Inter Tight', sans-serif;
      font-size: 11px;
      font-style: italic;
      letter-spacing: 0.04em;
      color: var(--ink-mute);
      margin: 0;
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
