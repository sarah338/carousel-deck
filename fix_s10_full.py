#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Headline text
html = html.replace(
    '24 months from pre-product to seed: 25K patients served, first clinic and employer pilots paying.',
    'Over 24 months, Carousel will go from pre-product to seed-ready &mdash; with first clinic and employer pilots paying and D2C retention proven.'
)

# 2. Fix CSS override that was blocking inline font-size
html = html.replace(
    '[data-screen-label="10 Traction"] .frame > .h1 { margin: 0 0 40px 0 !important; font-size: 64px !important; }',
    '[data-screen-label="10 Traction"] .frame > .h1 { margin: 0 0 16px 0 !important; font-size: 46px !important; }'
)

# 3. TEAM Mo.1-3: replace third bullet
html = html.replace(
    '          <li>In active discussions with 2&ndash;4 Chief Medical Officer candidates</li>',
    '          <li>Founding Clinical Advisor in active conversation (senior REI, NYC clinic).</li>'
)

# 4. TEAM Mo.4-10: replace first bullet
html = html.replace(
    '          <li>Fractional Chief Medical Officer signed</li>',
    '          <li>Founding Clinical Advisor formalized. Clinical advisory board (2&ndash;3 members) seated.</li>'
)

# 5. PRODUCT Mo.18-24: replace third bullet
html = html.replace(
    '          <li>Brand recognition in category</li>',
    '          <li>Top-of-mind brand in NYC fertility community; measurable digital and social awareness in target demographic.</li>'
)

# 6. PARTNERSHIPS Mo.1-3: replace both bullets
html = html.replace(
    '          <li>Meetings with Weill Cornell top RE</li>\n          <li>Meetings with Dr. Brian Levine, CCRM</li>',
    '          <li>Active dialogue with senior REI at leading NYC fertility clinic &mdash; design partner candidate.</li>\n          <li>Outreach to Weill Cornell and CCRM senior REs underway.</li>'
)

# 7. PARTNERSHIPS Mo.4-10: was empty, now has content
html = html.replace(
    '      <div class="trc-cell trc-cell-empty"></div>\n      <!-- Months 11-17 and 18-24 partnerships kept as-is below -->',
    '      <div class="trc-cell">\n        <ul class="trc-list">\n          <li>1&ndash;2 design partner clinics formalized; engagement data flowing into Carousel platform.</li>\n          <li>Initial conversations with benefits brokers (Mercer, Gallagher) initiated.</li>\n        </ul>\n      </div>'
)

# 8. PARTNERSHIPS Mo.11-17: second bullet — signed → late-stage negotiation
html = html.replace(
    '          <li>First employer benefits pilot signed at $10 PEPM</li>',
    '          <li>First employer benefits pilot in late-stage negotiation at $10 PEPM.</li>'
)

# 9. PARTNERSHIPS Mo.18-24: second bullet — conservative employer range
html = html.replace(
    '          <li>3&ndash;5 employer pilots converted to paid</li>',
    '          <li>1&ndash;2 employer pilots converted to paid at $10 PEPM.</li>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done.")
