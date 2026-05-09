#!/usr/bin/env python3
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. New headline
html = html.replace(
    'D2C now. Clinic in parallel. Employer at scale.',
    'Carousel pairs a patient app with a clinic platform, sold to patients now, clinics in parallel, and employers at scale.'
)

# 2. Delete sub-headline line
html = html.replace(
    '\n    <p class="bm5-sub">One product. Two layers. Three buyers &mdash; each channel earns the next.</p>\n',
    '\n'
)

# 3. Top padding: 48 → 72 (align with slides 7 & 8)
html = html.replace(
    '  <div class="frame" style="padding-top: 48px;">\n\n    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>',
    '  <div class="frame" style="padding-top: 72px;">\n\n    <p class="eyebrow" style="margin-bottom: 12px; color: var(--accent);">Business model</p>'
)

# 4. Increase margin-bottom on h1 to breathe without sub-headline
html = html.replace(
    '<h1 class="h1" style="margin: 0 0 6px; max-width: 1700px; font-size: 56px; line-height: 1.08;">Carousel pairs a patient app',
    '<h1 class="h1" style="margin: 0 0 16px; max-width: 1700px; font-size: 56px; line-height: 1.1;">Carousel pairs a patient app'
)

# Also update the CSS override margin
html = html.replace(
    '[data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 6px 0 !important; font-size: 56px !important; }',
    '[data-screen-label="09 Business model"] .frame > .h1 { margin: 0 0 16px 0 !important; font-size: 52px !important; }'
)

# 5. D2C path: flat from Mo.0–Mo.6, then ramps (fixes both the "thick at start"
#    and the "MO. 18 label covered" issues — top at Mo.18 now y=55, not y=22)
html = html.replace(
    'M 80,132 C 210,130 330,122 430,117 C 505,112 545,102 605,95 C 670,85 715,74 780,70 C 905,50 995,30 1130,22 C 1235,17 1350,15 1480,15 L 1480,140 L 80,140 Z',
    'M 80,140 C 180,140 340,140 430,139 C 500,138 548,128 605,118 C 665,108 715,95 780,88 C 905,70 1010,58 1130,52 C 1240,46 1365,38 1480,35 L 1480,140 L 80,140 Z'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done.")
