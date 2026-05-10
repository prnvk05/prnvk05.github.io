# CLAUDE.md — Portfolio Project Context

This file gives Claude Code full context on this project. Read it before making any changes.

---

## Who this is for

**Pranav Kanuparthi** — Senior ML Engineer, inventor, AGI builder.
- Email: pranavkanuparthi@gmail.com
- Phone: (469) 678-9877
- GitHub: prnvk05
- LinkedIn: pranavkanuparthi
- Location: Pittsburgh, PA

---

## The site

**Live URL:** pranavkanuparthi.com  
**Hosting:** GitHub Pages (repo: prnvk05.github.io)  
**Stack:** Single-file HTML/CSS/JS — no framework, no build step, no dependencies except Google Fonts

The entire site lives in `index.html`. Do not split it into multiple files unless explicitly asked.

---

## Design system

| Token | Value |
|-------|-------|
| Background | `#0a0a0a` |
| Surface | `#111111` |
| Border | `#1e1e1e` |
| Border light | `#2a2a2a` |
| Text | `#e8e4dc` |
| Text muted | `#6b6760` |
| Text dim | `#9d9890` |
| Accent | `#c8f55a` |
| Accent dim | `rgba(200, 245, 90, 0.10)` |

**Fonts** (loaded from Google Fonts):
- Display: `Syne` (700, 800)
- Mono: `DM Mono` (300, 400, 500)
- Body: `DM Sans` (300, 400, 500)

**Rules:**
- Never use em dashes (`—`) anywhere in copy. Use colons, commas, or full stops instead
- Bullets in lists use `▸` not `—`
- No inline styles except where unavoidable (e.g. padding-top on hero)
- All section numbers are zero-padded: 00, 01, 02...

---

## Site sections (in order)

| # | ID | Title |
|---|-----|-------|
| Fixed | `.agi-banner` | Scrolling AGI mission ticker |
| Fixed | `nav` | Navigation |
| — | `#hero` | Name, bio, stat grid |
| 00 | `#traits` | What I Bring + skills marquee |
| 01 | `#skills` | Tech stack (4 columns) |
| 02 | `#experience` | TDK SensEI, CMU, Wellnesys |
| 03 | `#projects` | 4 project cards |
| 04 | `#patents` | 5 patents + 2 publications |
| 05 | `#education` | CMU M.S. + RV College B.E. |
| 06 | `#credentials` | CES Award + certifications |
| 07 | `#life` | Beyond the Terminal (hobbies mosaic) |
| — | `#contact` | Contact + links |

---

## Brand identity

**North star:** Building AGI — intelligent systems that understand, act, and collaborate with humans.

**Brand line:** "The engineer you call when the problem doesn't have a solution yet."

**Traits to reinforce:**
1. Navigates ambiguity with confidence
2. Rapid prototyper
3. First-principles engineer
4. Full-stack ML builder (sensor to cloud)
5. Mission-oriented, not task-oriented
6. Builder of teams and culture

---

## Professional background

**TDK SensEI** (formerly Qeexo) — Sep 2021 to present, Pittsburgh PA
- Senior ML Engineer
- Multi-agent AI system for industrial asset diagnostics (AWS Bedrock, LangChain, LangGraph)
- $20M annual downtime savings for manufacturing clients
- 62% memory reduction, 20% latency improvement in data pipelines
- ARM DevSummit 2024 speaker: brighttalk.com/webcast/17792/598483

**Carnegie Mellon University** — May to Dec 2020
- Graduate Research Assistant, Neuromorphic Computer Architecture Lab
- Advisor: Prof. John Shen
- Temporal Neural Network (TNN) architectures, 73% on Spoken MNIST

**Wellnesys Inc.** — Oct 2018 to Jan 2020, Bangalore India
- Co-Founder and Chief Innovation Officer
- YogiFi: CES Innovation Award-winning AI + pressure sensor platform
- 98% yoga pose classification accuracy
- 12-member cross-functional team

---

## Education

- Carnegie Mellon University — M.S. Electrical and Computer Engineering, specialised in ML — May 2021
- RV College of Engineering — B.E. Electronics and Instrumentation Engineering — May 2017

---

## Patents

| Title | Status | ID |
|-------|--------|-----|
| System and non-intrusive method for exercise posture detection | Granted | US 20200254299 A1, IN 201941005350 |
| System and method to monitor an exercise posture of at least one user | Granted | IN 201841006784, WO 2019162743A1 |
| A flexible substrate and a method thereof | Granted | IN 201841006773, WO 2019162742A1 |
| System and method for performance evaluation of an exercise performed by a user | Pending | IN 202041000701 |
| Real-time offside offense determination system and a method thereof | Pending | IN 201841046250 |

**Publications/Talks:**
- Embedded ML for Industrial IoT Applications — ARM DevSummit 2024
- The Changing Nature of Human Adjudication — ITSMTGPD 2019, IEEE Technology and Society Magazine

---

## Skills

- **Knowledge:** Deep Learning, Machine Learning, Agentic AI Systems, Sensor Systems Dev., Data Analytics
- **Frameworks:** PyTorch, TensorFlow, Keras, LangChain, LangGraph, PySpark, NumPy, Pandas, Scikit-Learn, Pydantic
- **Cloud:** AWS Bedrock, Lambda, S3, DynamoDB, ECR, Docker
- **Languages:** Python, C/C++, SQL

---

## Hobbies (Life section)

Sailing (US Sailing certified), Motorsport, Sporting Clays, Boxing, Gaming, Reading

The life section (`#life`) uses a 2-row photo mosaic grid + a full-width quote panel.
Photo placeholders are in place — replace `life-tile-placeholder` divs with `<img class="life-tile-img">` when real photos are available.

---

## Links

- Resume (Google Drive): https://drive.google.com/file/d/1uS7PuvZ6ZcvtGFDEi8jyIaxUTA9T_DV6/view?usp=sharing
- ARM DevSummit talk: https://brighttalk.com/webcast/17792/598483
- GitHub: https://github.com/prnvk05
- LinkedIn: https://www.linkedin.com/in/pranavkanuparthi/
- Instagram: https://www.instagram.com/pranavkanuparthi/
