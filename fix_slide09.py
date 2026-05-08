#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix EMPLOYER clipping: x=72 → x=98 for all three left labels
html = html.replace(
    '<text x="72" y="74" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="#954A2D">D2C</text>',
    '<text x="98" y="74" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="#954A2D">D2C</text>'
)
html = html.replace(
    '<text x="72" y="197" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="#A06432">CLINIC</text>',
    '<text x="98" y="197" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="#A06432">CLINIC</text>'
)
html = html.replace(
    '<text x="72" y="312" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.52)">EMPLOYER</text>',
    '<text x="98" y="312" text-anchor="end" font-family="Inter Tight, sans-serif" font-size="11" font-weight="700" letter-spacing="3" fill="rgba(149,74,45,0.52)">EMPLOYER</text>'
)

# 2. Replace the three text blocks with enriched content
old_cols = """    <!-- THREE TEXT BLOCKS -->
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
    </div>"""

new_cols = """    <!-- THREE TEXT BLOCKS -->
    <div class="bm5-cols">
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch1">D2C &mdash; $20 / month</p>
        <p class="bm5-body">Convert WhatsApp beta to paid. Ship Maeve AI, community &amp; education library. Founder-led growth.</p>
        <p class="bm5-why2">Lowest cost, highest leverage. Founder&ndash;market fit drives early conversion.</p>
        <p class="bm5-proof">WhatsApp beta already live. LinkedIn audience growing 11K &rarr; 25K.</p>
      </div>
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch2">Clinic SaaS &mdash; $35&ndash;50K ACV</p>
        <p class="bm5-body">2&ndash;3 design partners from day one. Paid pilots at Mo. 9 using D2C engagement data as proof.</p>
        <p class="bm5-why2">Clinic sales cycles are 6&ndash;9 months. Relationships start now, revenue follows.</p>
        <p class="bm5-proof">Active conversation with Dr. Joshua Klein, Extend Fertility (NYC).</p>
      </div>
      <div class="bm5-col">
        <p class="bm5-ch bm5-ch3">Employer Benefits &mdash; $10 PEPM</p>
        <p class="bm5-body">First conversations at Mo. 12+. Close via Mercer &amp; Gallagher post-seed. Distinct from Maven/Carrot.</p>
        <p class="bm5-why2">Enterprise buyers need consumer brand AND clinical credibility before saying yes.</p>
        <p class="bm5-proof">D2C usage data + clinic logos = the enterprise pitch.</p>
      </div>
    </div>"""

html = html.replace(old_cols, new_cols)

# 3. Replace footer with promoted two-line math strip
old_foot = """    <!-- FOOTER -->
    <p class="bm5-foot"><em>~400K U.S. fertility patients annually &middot; 10% blended penetration &middot; $300/patient/year = $12M ARR opportunity &middot; Pre-seed milestone: $500K+ ARR run-rate by seed round.</em></p>
    <p class="bm5-src">U.S. patient volume: SART 2023 &middot; Pricing: women&rsquo;s health and digital health subscription benchmarks</p>"""

new_foot = """    <!-- FOOTER -->
    <div class="bm5-mktstrip">
      <p class="bm5-mktline">Addressable market: ~400K U.S. fertility patients annually &middot; ~10% blended penetration &middot; ~$300/patient/year = <strong>$12M ARR opportunity</strong>.</p>
      <p class="bm5-mktline">Pre-seed milestone: $500K+ ARR run-rate by seed round.</p>
    </div>
    <p class="bm5-src">U.S. patient volume: SART 2023 &middot; Pricing: women&rsquo;s health and digital health subscription benchmarks</p>"""

html = html.replace(old_foot, new_foot)

# 4. Update CSS: add bm5-why2, bm5-proof, bm5-mktstrip, bm5-mktline; remove bm5-why; remove bm5-foot
old_css = """    .bm5-why {
      font-family: 'Instrument Serif', serif; font-style: italic;
      font-size: 15px; color: var(--ink-mute); margin: 0; line-height: 1.4;
    }

    .bm5-foot {
      font-family: 'Instrument Serif', serif; font-size: 16px;
      color: var(--ink-soft); margin: 0 0 4px; line-height: 1.5;
    }
    .bm5-src {"""

new_css = """    .bm5-why2 {
      font-family: 'Inter Tight', sans-serif; font-size: 13px; font-weight: 400;
      color: var(--ink-soft); margin: 0 0 4px; line-height: 1.5;
    }
    .bm5-proof {
      font-family: 'Instrument Serif', serif; font-style: italic;
      font-size: 14px; color: var(--ink-mute); margin: 0; line-height: 1.45;
    }

    .bm5-mktstrip {
      border-top: 1px solid rgba(149,74,45,0.14);
      padding-top: 10px; margin-bottom: 6px;
    }
    .bm5-mktline {
      font-family: 'Instrument Serif', serif; font-size: 17px;
      color: var(--ink-soft); margin: 0 0 2px; line-height: 1.45;
    }
    .bm5-mktline strong { color: var(--accent); font-weight: 400; }
    .bm5-src {"""

html = html.replace(old_css, new_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done.")
