#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_slide = """<section class="slide" data-screen-label="09 Business model">
  <div class="pageno"><svg><use href="#mark"/></svg>09 / 11</div>
  <div class="frame" style="padding-top: 64px; display: flex; flex-direction: column;">

    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>
    <h1 class="h1" style="margin: 0 0 28px; max-width: 1700px; font-size: 52px; line-height: 1.1;">Carousel pairs a patient app with a clinic platform,<br>sold to patients now, clinics in parallel, and employers at scale.</h1>

    <!-- THREE-PHASE CASCADE -->
    <div class="ph-cols">

      <!-- Mo. 0–9: D2C only -->
      <div class="ph-col">
        <p class="ph-period">Mo. 0 &ndash; 9</p>
        <div class="ph-blocks">
          <div class="ph-block ph-d2c">
            <p class="ph-ch">D2C</p>
            <p class="ph-price">$20 / month</p>
          </div>
        </div>
        <div class="ph-foot">
          <p class="ph-arr">$180K &ndash; $360K ARR</p>
          <p class="ph-ms">1,500 &ndash; 2,500 subscribers</p>
        </div>
      </div>

      <!-- Divider -->
      <div class="ph-arrow">&rarr;</div>

      <!-- Mo. 9–18: D2C + Clinic -->
      <div class="ph-col">
        <p class="ph-period">Mo. 9 &ndash; 18</p>
        <div class="ph-blocks">
          <div class="ph-block ph-clinic">
            <p class="ph-ch">Clinic</p>
            <p class="ph-price">$35 &ndash; 50K ACV</p>
          </div>
          <div class="ph-block ph-d2c">
            <p class="ph-ch">D2C</p>
            <p class="ph-price">$20 / month</p>
          </div>
        </div>
        <div class="ph-foot">
          <p class="ph-arr">+ ~$70K clinic ARR</p>
          <p class="ph-ms">2 &ndash; 3 paid pilots. D2C data earns the pitch.</p>
        </div>
      </div>

      <!-- Divider -->
      <div class="ph-arrow">&rarr;</div>

      <!-- Mo. 18+: All three -->
      <div class="ph-col">
        <p class="ph-period">Mo. 18+</p>
        <div class="ph-blocks">
          <div class="ph-block ph-employer">
            <p class="ph-ch">Employer</p>
            <p class="ph-price">$10 PEPM</p>
          </div>
          <div class="ph-block ph-clinic">
            <p class="ph-ch">Clinic</p>
            <p class="ph-price">$35 &ndash; 50K ACV</p>
          </div>
          <div class="ph-block ph-d2c">
            <p class="ph-ch">D2C</p>
            <p class="ph-price">$20 / month</p>
          </div>
        </div>
        <div class="ph-foot">
          <p class="ph-arr">$500K+ combined at seed</p>
          <p class="ph-ms">1 &ndash; 2 employer pilots. Clinic logos unlock enterprise.</p>
        </div>
      </div>

    </div><!-- /ph-cols -->

    <div class="ph-mktstrip">
      <p class="ph-mktline">Addressable market: ~400K U.S. fertility patients annually &middot; ~10% blended penetration &middot; ~$200&ndash;$250/patient/year = <strong>~$9M ARR opportunity</strong>.</p>
    </div>
    <p class="ph-src">U.S. patient volume: SART 2023 &middot; Pricing: women&rsquo;s health and digital health subscription benchmarks</p>

  </div>
  <div class="confidential">Carousel 2026 &middot; Confidential</div>
  <style>
    [data-screen-label="09 Business model"] .frame { display: flex; flex-direction: column; }
    [data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 28px 0 !important; font-size: 52px !important; }

    /* Column layout */
    .ph-cols { display: flex; align-items: flex-start; gap: 0; flex: 1; min-height: 0; margin-bottom: 16px; }
    .ph-col { flex: 1; display: flex; flex-direction: column; }
    .ph-arrow { flex: 0 0 48px; display: flex; align-items: center; justify-content: center; font-size: 32px; color: rgba(149,74,45,0.28); padding-top: 56px; }

    /* Column header */
    .ph-period {
      font-family: 'Inter Tight', sans-serif; font-size: 13px; font-weight: 700;
      letter-spacing: 0.20em; text-transform: uppercase; color: var(--ink-mute);
      margin: 0 0 12px; padding-bottom: 10px;
      border-bottom: 1.5px solid rgba(149,74,45,0.18);
    }

    /* Stacked blocks */
    .ph-blocks { display: flex; flex-direction: column; gap: 6px; height: 400px; margin-bottom: 16px; }
    .ph-block {
      flex: 1; display: flex; flex-direction: column; justify-content: center;
      padding: 0 28px; border-left: 5px solid transparent;
    }
    .ph-d2c    { background: rgba(125,56,32,0.08);  border-left-color: #7D3820; }
    .ph-clinic { background: rgba(139,85,32,0.10);  border-left-color: #8B5520; }
    .ph-employer { background: rgba(191,112,48,0.10); border-left-color: #BF7030; }

    /* Block text */
    .ph-ch {
      font-family: 'Inter Tight', sans-serif; font-size: 14px; font-weight: 700;
      letter-spacing: 0.20em; text-transform: uppercase; margin: 0 0 6px;
    }
    .ph-d2c .ph-ch     { color: #7D3820; }
    .ph-clinic .ph-ch  { color: #8B5520; }
    .ph-employer .ph-ch { color: #BF7030; }

    .ph-price {
      font-family: 'Instrument Serif', serif; font-size: 34px; line-height: 1.1; margin: 0;
    }
    .ph-d2c .ph-price    { color: #7D3820; }
    .ph-clinic .ph-price { color: #8B5520; }
    .ph-employer .ph-price { color: #BF7030; }

    /* Footer below blocks */
    .ph-foot { border-top: 1px solid rgba(149,74,45,0.14); padding-top: 12px; }
    .ph-arr {
      font-family: 'Instrument Serif', serif; font-size: 22px; color: var(--ink);
      margin: 0 0 4px; line-height: 1.2;
    }
    .ph-ms {
      font-family: 'Inter Tight', sans-serif; font-size: 14px; font-weight: 300;
      color: var(--ink-mute); margin: 0; line-height: 1.4;
    }

    /* Bottom strip */
    .ph-mktstrip { border-top: 1.5px solid rgba(149,74,45,0.18); padding-top: 10px; margin-bottom: 5px; margin-top: auto; }
    .ph-mktline { font-family: 'Inter Tight', sans-serif; font-size: 15px; font-weight: 400; color: var(--ink-soft); margin: 0; line-height: 1.5; }
    .ph-mktline strong { color: var(--accent); font-weight: 700; }
    .ph-src { font-family: 'Inter Tight', sans-serif; font-size: 11px; font-style: italic; letter-spacing: 0.04em; color: var(--ink-mute); margin: 0; }
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
