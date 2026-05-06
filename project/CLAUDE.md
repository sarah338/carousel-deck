# Carousel Pre-Seed Pitch Deck — Project Context

This file is the persistent brief. Read it at the start of every chat in this project.

## What this is

A 10-slide pre-seed pitch deck for **Carousel** — a fertility companion product (education, community, emotional support) for women navigating egg freezing, IVF, and fertility decisions in the years between "old enough to start preserving" and "ready to use what you preserved."

**Audience:** pre-seed VCs.
**Tone:** literary, considered, warm. Not Silicon-Valley-slick. Not clinical. Not "femtech pastel."
**Primary file:** `Carousel Pre-Seed Deck.html`. Versioned snapshots (`-pre-typeramp`, `-pre-narrative`, etc.) are restore points — do not edit them, do not show them to the user unless asked.

## Slide map (1-indexed; matches `data-screen-label`)

1. Cover — split layout, dark portrait left / cream type right
2. Opening — "Why now," 49% stat, the "defining decade" framing (NYT data)
3. Premise — "Fertility medicine works. The experience around it is broken."
4. Voice of the patient — verbatim quotes from 30 interviews (NYU Langone, Weill Cornell, etc.)
5. Introducing Carousel — three pillars: Education / Community / Emotional Support
6. Market — patient-volume stat (citation pending) + nested-bubble TAM/SAM/SOM
7. Go to market — three-card phased GTM (deep / mid / pale clay)
8. Competition — **3 variants live** (`v-a` timeline, `v-b` 2x2, `v-c` capability matrix). Default is `v-c`. Switcher lives in Tweaks.
9. Team — bios + grayscale logo row (Amazon, Amex, SonderMind, Northwestern)
10. The ask

## Design system — locked

**Colors** (CSS vars in `:root`):
- `--bg: #F7F1E4` (cream) · `--bg-card: #EFE7D5`
- `--ink: #4A382A` (warm dark brown — NEVER pure black) · `--ink-soft: #6B5848` · `--ink-mute: #9A8978`
- `--accent: #954A2D` (clay — the single emphasis color, used for eyebrows + accents) · `--accent-soft: #C99477` · `--accent-pale: #E8D5C4`
- Rules: `rgba(42,32,24,0.18)` / `0.08`

**Type ramp** (do not invent new sizes — pick from this ramp):
- `.display` — Instrument Serif 192/0.96, -0.015em — cover only
- `.h1` — Instrument Serif 88/1.08, -0.014em — slide titles (often overridden to 64px on text-dense slides; that's intentional)
- `.h2` — Instrument Serif 48/1.12
- `.quote` — Instrument Serif 48/1.22 upright (NOT italic)
- `.pull` — Instrument Serif 32/1.35 upright — ledes & sub-heads
- `.body-lg` — Inter Tight 24/1.5 weight 300
- `.body` — Inter Tight 22/1.5 weight 300, color `--ink-soft`
- `.eyebrow` — Inter Tight 14, 0.24em tracking, uppercase, `--ink-mute` (but on slide titles, eyebrow turns `--accent`)
- `.stat` — Instrument Serif, big numbers, -0.02em
- `.quote-attr` — Inter Tight 14, 0.22em tracking, uppercase, `--ink-mute`

**Fonts:** Instrument Serif (headlines, quotes, stats — upright unless explicitly italic for sources/citations). Inter Tight 300/400/500 (body, eyebrows, UI). Italic Instrument Serif is reserved for source lines and the cover Joni Mitchell epigraph.

**Layout primitives:**
- Slide container: `<section class="slide" data-screen-label="NN Title">` with `<div class="frame">` inside
- Page number: `.pageno` bottom-right, "NN / 10" with the carousel mark SVG (`<use href="#mark"/>`)
- Confidential mark: `.confidential` bottom-left, "Carousel 2026 · Confidential"
- Source citations: `.source` top-right OR small italic Instrument Serif line under the relevant stat
- Standard slide padding is 110px sides / 56px bottom (matches pageno/confidential anchors)
- Eyebrow → h1 → pull → content is the canonical vertical rhythm

**Don't:**
- Don't use emoji.
- Don't use gradients on backgrounds.
- Don't add icons unless they earn their place.
- Don't put citations in the top-right of slide 6 (we tried; it crowds the bubble chart). Put citations under the stat, small italic.
- Don't introduce a second accent color. Clay (`#954A2D`) is the only emphasis color.
- Don't use pure black. Ink is warm brown.
- Don't reference cross-project files as URLs in the HTML — copy them into `assets/` first.

## Infrastructure

- Slide shell: `deck-stage.js` (the deck_stage starter component, sitting at project root). Auto-tags slides, handles scaling, posts `slideIndexChanged` for speaker notes.
- Speaker notes: `<script type="application/json" id="speaker-notes">` in `<head>`. Array indexed by slide.
- Tweaks panel: live, includes the Slide 8 variant switcher (a/b/c). Honor the Tweaks protocol — listener registered before announcing availability.
- Print version: `Carousel Pre-Seed Deck-print.html` is a separate PDF-friendly export. If the main deck changes structurally, the print file likely needs a re-sync — ask before assuming it's current.
- Snapshot discipline: before any large edit (type ramp change, narrative reshuffle, slide-8 variant pivot), copy the current main file to `Carousel Pre-Seed Deck-pre-<reason>.html` first.

## Voice & copy

- Headlines are full sentences with periods. Two-line headlines use a hard `<br/>`.
- "She" / "her" — Carousel speaks about the user as a person, not a "user."
- No buzzwords: avoid "empower," "journey," "ecosystem," "unlock," "platform" (in headlines).
- The Joni Mitchell epigraph on the cover is load-bearing for the brand voice. It stays.
- Stats always cite source; pending citations get an explicit "[pending citation]" eyebrow until resolved.

## Working agreements with Sarah

- Show the file early; iterate in place. Don't rebuild from scratch.
- Variations explored in tweaks/variants live in the same file when possible.
- When asked for "a new version," copy-then-edit and keep the snapshot.
- Speaker notes only when explicitly requested.
- Slide 8 still has 3 live variants; final pick is deferred.
- Slide 6 stat is still pending a real citation.

## Open threads (as of last session)

- Slide 6 — real patient-volume citation needed
- Slide 8 — pick one of v-a/v-b/v-c and remove the other two before final send
- Print export — verify it matches the current main deck before any external share
