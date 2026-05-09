#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── SLIDE 9 ──────────────────────────────────────────────────────────────────

# 1. SVG: D2C right-edge annotation — ARR range + metric rename
html = html.replace(
    '<text x="1518" y="70" font-family="Instrument Serif, serif" font-size="30" fill="#7D3820">$360K&#x2013;$600K ARR</text>',
    '<text x="1518" y="70" font-family="Instrument Serif, serif" font-size="30" fill="#7D3820">$180K&#x2013;$360K ARR</text>'
)
html = html.replace(
    '<text x="1518" y="94" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(125,56,32,0.60)">1,500&#x2013;2,500 SUBSCRIBERS</text>',
    '<text x="1518" y="94" font-family="Inter Tight, sans-serif" font-size="12" letter-spacing="2" fill="rgba(125,56,32,0.60)">1,500&#x2013;2,500 PATIENTS SERVED</text>'
)

# 2. D2C text block — replace activity line with wedge/moat reframe
html = html.replace(
    '<p class="bm5-body">Convert WhatsApp beta to paid. Ship Maeve AI, community &amp; education library. Founder-led growth.</p>\n        <p class="bm5-proof">WhatsApp beta live. LinkedIn audience: 11K &rarr; 25K.</p>',
    '<p class="bm5-body">D2C is the wedge &mdash; not the moat. Patients pay during their active fertility journey, generating the engagement data that earns clinic and employer revenue.</p>\n        <p class="bm5-proof">WhatsApp beta live. LinkedIn audience: 11K &rarr; 25K.</p>'
)

# 3. Bottom math: $300 → $200–250, $12M → ~$9M
html = html.replace(
    '~$300/patient/year = <strong>$12M ARR opportunity</strong>',
    '~$200&ndash;$250/patient/year = <strong>~$9M ARR opportunity</strong>'
)

# ── SLIDE 10 ─────────────────────────────────────────────────────────────────

# 4. Headline — new longer, honest version
html = html.replace(
    '<h1 class="h1" style="margin: 0 0 12px; max-width: 1620px; font-size: 72px; line-height: 1.05;">\n      From signal to scale.\n    </h1>',
    '<h1 class="h1" style="margin: 0 0 12px; max-width: 1620px; font-size: 46px; line-height: 1.15;">24 months from pre-product to seed: 25K patients served, first clinic and employer pilots paying.</h1>'
)

# 5. Product row Mo.11–17: downloads → patients served, activation → range
html = html.replace(
    '          <li>10K&ndash;25K downloads</li>\n          <li>60%+ activation</li>\n          <li>Defensible cohort retention curves</li>',
    '          <li>15&ndash;25K patients served across waitlist, beta community, and paid product</li>\n          <li>40&ndash;60% activation by Month 17, benchmarked against peer set</li>\n          <li>Defensible cohort retention curves published</li>'
)

# 6. Partnerships Mo.18–24: drop $500K+ ARR / NRR claim → honest range
html = html.replace(
    '          <li>Clinic SaaS: $500K+ signed ARR, NRR &gt; 100%</li>',
    '          <li>Clinic SaaS: $100&ndash;300K signed ARR across 2&ndash;3 paid pilots</li>'
)

# 7. Fundraising row: drop Series A from Mo.11–17 slot; add post-Mo.24 note
html = html.replace(
    '      <div class="trc-cell trc-cell-raise" style="justify-content: flex-end;">Series A</div>\n      <div class="trc-cell trc-cell-empty"></div>',
    '      <div class="trc-cell trc-cell-empty"></div>\n      <div class="trc-cell trc-cell-raise-future">Series A targeted post-Month 24, contingent on milestone delivery.</div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done.")
