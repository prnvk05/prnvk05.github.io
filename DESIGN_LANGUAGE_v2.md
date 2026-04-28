# Design Language — Pranav Kanuparthi Personal Brand

Version 2.0 · April 2026

---

## Who this is for

This document defines the visual and verbal identity for pranavkanuparthi.com and any future brand touchpoints. It exists so that any designer, developer, or AI assistant working on this brand can make consistent decisions without needing to ask.

---

## Brand Identity

### The one-liner

> "The engineer you call when the problem doesn't have a solution yet."

### What this brand is

Pranav is a **maker**: someone who builds things that don't exist yet. Not just software. Hardware platforms, companies, patents, systems. The brand should feel like the person — technically serious, deeply curious, and genuinely human. It should never feel corporate, polished to the point of sterility, or like it was generated from a template.

### The three brand pillars

**1. Maker, not just engineer**
The identity leads with building things, not with job titles or tech stacks. Patents, startups, sensor platforms, agent architectures — this is the story of someone who creates. Every section should reinforce that making is an instinct, not a job description.

**2. Human and approachable**
The copy sounds like a real person talking, not a LinkedIn profile. Short sentences. First person. Honest opinions. No buzzword clusters. The tone is confident but never arrogant — like a senior engineer you'd actually want to have a beer with.

**3. Mission-driven**
Everything connects back to a north star: building AGI, and specifically applying it to the physical world. This isn't decoration. It should be the first thing someone understands about Pranav when they land on the site.

---

## Visual Language

### Colour palette

| Name | Hex | Usage |
|------|-----|-------|
| Background | `#f5f2ed` | Page background — warm off-white |
| Surface | `#ede9e2` | Cards, panels, elevated surfaces |
| Border | `#dbd5cc` | Default borders and dividers |
| Border light | `#e2ddd5` | Hover states, secondary borders |
| Text | `#111111` | Primary readable text |
| Text dim | `#666666` | Secondary text, descriptions |
| Text muted | `#888880` | Labels, meta, timestamps |
| Ferrari Red | `#FF2800` | Primary accent. CTAs, hero name highlight, stat numbers |
| Ferrari Red dim | `rgba(255, 40, 0, 0.08)` | Accent backgrounds, highlight states |
| Miami Blue | `#0096FF` | Secondary accent. Section labels, eyebrows, dates, nav logo |
| Miami Blue dim | `rgba(0, 150, 255, 0.08)` | Blue accent backgrounds |
| Bright Green | `#00d46a` | Status only. Granted patents, confirmed states |
| Bright Green dim | `rgba(0, 200, 100, 0.12)` | Green status backgrounds |

### Colour usage rules

**Ferrari Red** leads on identity and action: hero name, primary CTA button, stat numbers, award badges, section accent bars on hover.

**Miami Blue** guides and informs: section eyebrows/labels, project numbers, experience dates, nav logo, hero eyebrow line.

**Bright Green** is reserved strictly for confirmed positive status — granted patents and verified accomplishments only. Do not use it decoratively.

The warm off-white background is foundational. It separates this design from dark-only portfolios and gives the red and blue room to breathe. All three accent colours work together only because the background is neutral.

### Typography

Three typefaces, each with a distinct role:

| Typeface | Variable | Role |
|----------|----------|------|
| Syne | `--font-display` | Headings, names, large display text |
| Space Mono | `--font-mono` | Labels, tags, metadata, UI elements, nav |
| DM Sans | `--font-body` | All body copy and descriptions |

**Syne** is the personality typeface. Use it for anything that needs weight and presence: section titles, the hero name, trait card titles, stat numbers, the contact heading.

**Space Mono** provides technical credibility and utility. It should feel like a terminal or spec sheet. Use it for section numbers, tags, eyebrows, dates, badges, and anything acting as metadata rather than content.

**DM Sans** is the workhorse. Light weight (300) for most body copy. It should never compete with Syne.

### Type scale

| Use | Size | Weight | Typeface |
|-----|------|--------|----------|
| Hero name | 56–112px (fluid, clamp) | 800 | Syne |
| Section title | 32–56px (fluid, clamp) | 800 | Syne |
| Trait/card title | 20px | 700 | Syne |
| Body copy | 16px | 300 | DM Sans |
| Card description | 13–14px | 300 | DM Sans |
| Labels / eyebrows | 9–11px | 400 | Space Mono |
| Stat numbers | 40px | 800 | Syne |

### Grid and spacing

- Section padding: `96px 80px` (desktop), `72px 24px` (mobile, max-width ~960px)
- Max content width: `1100px`, centred
- Card gap: `1px` with `background: var(--border)` on the parent container — creates razor-thin separators
- Border width: `1px` throughout
- Accent bar on hover: `2px` top border, scales in from left using `transform: scaleX()`
- Base unit: `8px`

### The 1px gap grid

Cards and grids use `gap: 1px` with a background colour on the parent set to the border colour. This creates seamless, precise separators that feel technical without heavy borders. This pattern is used for: trait cards (3×2), project cards (2×2), life mosaic, skills groups. Preserve it everywhere.

### Grid background (page texture)

A fine blueprint grid sits fixed behind the entire page:

```css
body::before {
  background-image:
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 24px 24px;
}
```

Grid colour: `rgba(0, 0, 0, 0.04)` — subtle on the off-white background, giving a technical, draughting-table quality. Grid size is **24px** — fine and tight, not coarse. Do not increase it above 30px.

### Hover behaviour

All interactive elements respond to hover in a restrained way:

- Cards: background shifts one step darker (e.g. surface to border tone)
- Accent bar: `2px` top line scales in from left using `transform: scaleX(0) → scaleX(1)`
- Links: colour shifts to Ferrari Red
- Nav links: colour shifts to Ferrari Red
- Nothing jumps, scales up, or bounces

Animation timing: `0.2s–0.35s ease` for most transitions. Nothing faster than `0.15s`.

---

## Voice and Tone

### The core principle

Write like a smart person talking to another smart person. Not like a company. Not like a recruiter wrote it. Not like a conference bio.

### What this sounds like

**Good:**
> "I'm a maker at heart. I build things that don't exist yet."

> "Nine years, one thread: making machines that genuinely understand their environment."

> "The same instinct that makes me build software also puts me on a sailboat or at a shooting range."

**Avoid:**
> "Seasoned ML professional with a demonstrated track record of delivering value-driven solutions..."

> "Passionate about leveraging cutting-edge AI to drive impactful outcomes..."

### Rules

**No em dashes.** Use commas, colons, full stops, or restructure the sentence.

**No buzzword clusters.** One strong noun beats three weak adjectives.

**Short sentences work.** Especially for punchy statements. Don't qualify everything.

**First person, present tense** for the traits and bio sections. "I build" not "He builds."

**Numbers beat adjectives.** "$20M in downtime savings" beats "significant cost reduction."

**Italics for the key thought.** In trait cards, the closing italicised phrase should be the sharpest, most memorable line. Everything else builds to it.

### Section-by-section tone

| Section | Tone |
|---------|------|
| AGI banner | Declarative. Present tense. Mission-first. |
| Hero bio | Personal, direct, human. Lead with identity, not job title. |
| What I Bring | Honest and specific. Traits backed by real evidence. |
| Experience | Precise and outcome-focused. Numbers where possible. |
| Projects | Concise problem statements. What it does and why it matters. |
| Beyond the Terminal | Warm and genuine. Not performative. |
| Contact | Warm but selective. "The right problem" not "any opportunity." |

---

## Layout Principles

### Page structure

The page flows top to bottom in this order:

1. **AGI banner** — scrolling marquee, mission statements
2. **Nav** — sticky, transparent blur
3. **Hero** — 50/50 two-column grid
4. **What I Bring** — 3×2 trait card grid
5. **Experience** — vertical list with metadata sidebar
6. **Projects** — 2×2 card grid
7. **Patents** — sidebar count + list
8. **Life** — asymmetric mosaic
9. **Skills** — 4-column group grid
10. **Contact** — 2-column with link list
11. **Footer**

### Section alternation

Sections alternate between `--black` (Background) and `--dark` (Surface) backgrounds. This creates rhythm as the user scrolls without needing dividers.

**Pattern:** hero (bg) → traits (bg) → experience (surface) → projects (bg) → patents (surface) → life (bg) → skills (surface) → contact (bg)

### Hero layout

The hero uses a 50/50 two-column grid. Left column: name, bio, CTAs. Right column: 2×2 stat grid + tagline quote. The stat grid creates visual weight on the right. The large ghost-text "MAKER" sits behind the hero content, outlined in Ferrari Red at very low opacity.

### Section header pattern

Every section uses the same header:

```
[section number in mono]  [Section Title in Syne]  [flex rule line]
```

The rule line is a `flex: 1` element with `height: 1px; background: var(--border)`. It aligns number and title to the left and creates a clean right edge.

### The impact chip pattern

For the main experience entry (TDK SensEI), key metrics are surfaced as chips below the bullet list. These use Ferrari Red accent colour (`--accent-glow` background, `--amber` text). Only use for hard numbers or awards — not soft accomplishments.

---

## Component Library

### AGI Banner

A fixed-height marquee (`36px`) at the very top of the page. Background is `--amber-glow`. Text in Space Mono at `0.68rem`, Ferrari Red, `uppercase`, `0.12em` letter-spacing. Messages are short, declarative, mission-connected. Separated by a small diamond `◆` glyph.

### Nav

Sticky, `56px` tall. Background `rgba(245, 242, 237, 0.9)` with `backdrop-filter: blur(16px)`. Left: logo in Space Mono, Ferrari Red. Centre: nav links in Space Mono, muted, hover to Ferrari Red. Right: Resume CTA — solid Ferrari Red background, dark text.

### Stat box

Used in the hero right column. A 2×2 grid using the 1px gap pattern. Each box: large Syne numeral in Ferrari Red, small Space Mono label in muted. A `2px` Ferrari Red underline animates in from left on hover.

### Trait card

Six cards in a 3×2 grid. Each: emoji, Space Mono label in muted, Syne title, DM Sans description. The closing italicised phrase is the most important element. `2px` top Ferrari Red bar scales in on hover.

### Experience item

Grid layout: `220px` meta column + `1fr` content column. Meta has a right border. Content has bullet list + impact chips. A `4px` right-edge bar animates to Ferrari Red on hover. Experience dates are in Miami Blue. Company badges use Ferrari Red accent dim.

### Project card

Cards in a 2×2 grid with 1px gap. Each: project number in Miami Blue, Syne title, DM Sans description, accent highlight line in Ferrari Red, tag pills with muted border. Arrow `↗` in top-right corner animates to Ferrari Red on hover.

### Patent item

Two-column grid: `80px` status badge + title and number. `granted` status: Ferrari Red accent background and text. `pending` status: muted border and muted text. `3 Granted` count in Bright Green. Patent count sidebar uses `6rem` Syne numeral in Ferrari Red.

### Life mosaic tile

Asymmetric grid: `7fr 5fr` columns, alternating which column gets the wider tile per row. Each tile: dark gradient overlay, emoji placeholder, label in Miami Blue, Syne title, DM Sans description. Overlay opacity: `0.78` always visible.

---

## Things to Never Do

- Use font weights above 800 or below 300
- Add shadows (the design is flat, uses borders instead)
- Use `border-radius` anywhere (everything is sharp-cornered)
- Make hover animations jump or scale up the whole card
- Write in third person for the bio or traits sections
- Add stock photography or illustrations
- Use Ferrari Red for body text
- Use Miami Blue for primary CTAs
- Use Bright Green for anything other than confirmed/granted status
- Use em dashes
- Break the single-file HTML structure without good reason
- Change the grid texture size above 30px
- Add more than three accent colours to the palette

---

## Future Considerations

When photos are added to the life mosaic tiles:
- Landscape-oriented, minimum 800px wide
- High contrast and active (not posed)
- They should work under a dark gradient overlay

The resume link in the nav (`.nav-cta`) points to a Google Drive PDF. Update the `href` whenever the resume changes.

The AGI banner messages can be updated as Pranav's work evolves. They should always be short, declarative, and mission-connected. Current messages: "Building AGI", "Applied to the physical world", "Machines that genuinely understand their environment."
