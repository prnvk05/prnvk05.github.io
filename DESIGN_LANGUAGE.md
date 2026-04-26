# Design Language — Pranav Kanuparthi Personal Brand

Version 1.1 · April 2025

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
The identity leads with building things, not with job titles or tech stacks. Patents, startups, sensor platforms, agent architectures — this is the story of someone who creates. Every section reinforces that making is an instinct, not a job description. The hero eyebrow reads "Building AGI · Maker · TDK SensEI". The traits lead with "Builder First, Engineer Second." The life section quote is "I make things. In the lab, on the water, in the ring, everywhere." Maker is the word — use it consistently.

**2. Human and approachable**
The copy sounds like a real person talking, not a LinkedIn profile. Short sentences. First person. Honest opinions. No buzzword clusters. The tone is confident but never arrogant — like a senior engineer you'd actually want to have a beer with.

**3. Mission-driven**
Everything connects back to a north star: building AGI, and specifically applying it to the physical world. This isn't decoration. It should be the first thing someone understands about Pranav when they land on the site.

---

## Visual Language

### Colour palette

| Name | Hex | Usage |
|------|-----|-------|
| Background | `#0a0a0a` | Page background |
| Surface | `#111111` | Cards, panels, elevated surfaces |
| Border | `#1e1e1e` | Default borders and dividers |
| Border light | `#2a2a2a` | Hover states, secondary borders |
| Text | `#e8e4dc` | Primary readable text |
| Text dim | `#9d9890` | Secondary text, descriptions |
| Text muted | `#6b6760` | Labels, meta, timestamps |
| Accent | `#c8f55a` | Brand colour. Use sparingly and deliberately |
| Accent dim | `rgba(200, 245, 90, 0.10)` | Accent backgrounds, highlight states |

The accent is the only colour on the page. Everything else is black, grey, and off-white. This makes every use of the accent feel intentional and high-value. Do not add new colours. Do not use the accent for decoration — only for meaning (active state, highlight, call to action, important data point).

### Typography

Three typefaces, each with a distinct role:

| Typeface | Variable | Role |
|----------|----------|------|
| Syne | `--display` | Headings, names, large display text |
| DM Mono | `--mono` | Labels, tags, metadata, UI elements, nav |
| DM Sans | `--sans` | All body copy and descriptions |

**Syne** is the personality typeface. It's what makes the site feel distinctive. Use it for anything that needs weight and presence: section titles, the hero name, trait card titles, the contact heading.

**DM Mono** provides technical credibility and utility. It should feel like it belongs in a terminal or a spec sheet. Use it for section numbers, tags, eyebrows, dates, and anything that acts as metadata rather than content.

**DM Sans** is the workhorse. Light weight (300) for most body copy. It should never compete with Syne — its job is to be clear and easy to read.

### Type scale (approximate)

| Use | Size | Weight | Typeface |
|-----|------|--------|----------|
| Hero name | 50–76px (fluid) | 800 | Syne |
| Section title | 26–40px (fluid) | 700 | Syne |
| Trait/card title | 20px | 700 | Syne |
| Body copy | 16px | 300 | DM Sans |
| Card description | 13–14px | 300 | DM Sans |
| Labels / eyebrows | 9–11px | 400–500 | DM Mono |
| Stat numbers | 38px | 800 | Syne |

### Grid and spacing

The site uses an informal 12-column grid for complex sections (life mosaic, project cards) and a consistent `96px 80px` section padding on desktop. The base unit is roughly 8px. Key values:

- Section padding: `96px 80px` (desktop), `72px 24px` (mobile)
- Card gap: `1px` (creates a seamless grid effect using a background colour trick)
- Border width: `1px` throughout
- Accent bar on hover: `2px` bottom border

### The 1px gap grid

Cards and grids use `gap: 1px` with a `background: var(--border)` on the parent. This creates razor-thin separators that feel precise and technical without heavy borders. It is one of the most recognisable visual patterns on the site. Preserve it.

### Hover behaviour

All interactive elements respond to hover in a restrained way:
- Cards: background lightens slightly (`--bg` to `--surface` or `--surface` to `#141414`)
- Accent bar: a `2px` bottom line scales in from left using `transform: scaleX()`
- Links: colour shifts to accent
- Nothing jumps, bounces, or draws excessive attention

Animation timing is `0.25–0.55s ease` for most transitions. Nothing faster than `0.15s`, nothing slower than `0.6s`.

### Noise texture

A subtle fractal noise overlay sits fixed over the entire page at `opacity: 0.022`. This prevents the flat dark background from feeling like a void and gives the site a tactile, printed quality. Do not remove it.

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

> "Results-oriented engineer with expertise across the full machine learning lifecycle..."

### Rules

**No em dashes.** Use commas, colons, full stops, or restructure the sentence.

**No buzzword clusters.** One strong noun beats three weak adjectives. "Maker" says more than "innovative, results-driven, cross-functional."

**Short sentences work.** Especially for punchy statements. Don't qualify everything.

**First person, present tense** for the traits and bio sections. "I build" not "He builds" or "Building."

**Numbers beat adjectives.** "$20M in downtime savings" is better than "significant cost reduction."

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

### Asymmetry is intentional

The hero is split 50/50 but the stat grid creates visual weight on the right. The life mosaic uses asymmetric column spans across a 12-column grid in two rows of 360px: row 1 is sailing (7/12) + motorsport (5/12), row 2 is sporting clays (5/12) + boxing (7/12). The dominant tiles — sailing and boxing — get 7 columns. This cross-diagonal asymmetry prevents the page from feeling templated. There are 4 life tiles total (sailing, motorsport, sporting clays, boxing), followed by a full-width quote tile.

### Section alternation

Sections alternate between `--bg` and `--surface` backgrounds. This creates a natural rhythm as the user scrolls and makes each section feel distinct without using dividers.

**Pattern:** traits (bg) → skills (surface) → experience (bg) → projects (surface) → patents (bg) → education (surface) → credentials (bg) → life (bg) → contact (bg)

### The impact chip pattern

For the main experience entry (TDK SensEI), key metrics are surfaced as chips below the bullet list. These use the accent colour and should only be used for hard numbers or awards — not for soft accomplishments.

---

## Component Library

### Section header

Every section uses the same header pattern:
```
[section number in mono]  [Section Title in Syne]  [rule line]
```
The rule line is a flex spacer with a 1px border. It aligns the number and title to the left and creates a clean right edge.

### Stat box

Used in the hero grid. A 2x2 grid of numbers. Each box has a large Syne numeral, a small DM Mono label, and an accent underline that animates in on hover. Use only for hard, impressive numbers.

### Trait card

Six cards in a 3x2 grid. Each has an emoji, a DM Mono label, a Syne title, and a DM Sans description. The closing italicised phrase is the most important element — it should be sharp enough to stand alone.

### Experience item

A three-column layout: company metadata on the left (bordered right edge), content in the centre, a 4px accent bar on the far right that animates to the accent colour on hover. Sub-roles are separated by a horizontal rule within the content column.

### Life mosaic tile

Full-height image containers with a gradient overlay. The overlay is always visible at `opacity: 0.78` and shifts to `opacity: 1` on hover. Title and description sit at the bottom of the overlay. Placeholder state shows an emoji and a hint.

---

## Things to Never Do

- Add a second accent colour
- Use em dashes
- Make hover animations jump or scale up the whole card
- Use font weights above 800 or below 300
- Add shadows (the design is flat and uses borders instead)
- Use `border-radius` anywhere (everything is sharp-cornered)
- Write in third person for the bio or traits sections
- Add stock photography or illustrations
- Use the accent colour for body text
- Break the single-file HTML structure without good reason

---

## Future Considerations

When photos are added to the life mosaic, they should:
- Be landscape-oriented, minimum 800px wide
- Be high contrast and work with a dark overlay
- Feel personal and active, not posed

The resume link in the nav should point to an up-to-date Google Drive PDF. Update the `href` on the `.nav-cta` element whenever the resume changes.

The AGI banner messages can be updated as Pranav's work evolves. They should always be short, declarative, and mission-connected.
