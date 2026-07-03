# 00 — Presentation: Basics of Software Engineering (from a Software Engineer)

The **opening talk for Day 1**. Before students write any Python, this gives them the mental map
of how real software is built: frontend, backend, API, database, Git, cloud, DevOps, CI/CD — and
where AI engineering fits on top.

**Audience:** 2nd/3rd-year college students, complete beginners. Heavy on analogies (restaurant,
"someone else's computer", "save game for code"), light on jargon.

## How to present it
It's a single self-contained HTML file — no install needed. (The **Plus Jakarta Sans** font
loads from Google Fonts when you're online; offline it falls back cleanly to the system font.)

1. Double-click **`index.html`** (opens in any browser), or right-click → Open with → your browser.
2. Press **F** for fullscreen (or the ⛶ button).
3. Navigate:
   - **→ / Space / click right half** → next slide
   - **← / click left half** → previous slide
   - **Home / End** → jump to first / last
   - A progress bar (top) and slide counter (bottom-left) track where you are.

Works great with a wireless presenter/clicker (its next/prev map to the arrow keys).

## Slide flow + speaker notes
21 slides, ~28–32 min with discussion. Suggested talking points:

| # | Slide | Talk about / ask the room |
|--:|-------|---------------------------|
| 1 | Title | "By the end you'll explain all 8 of these badges to a friend." |
| 2 | Why start here | AI apps are still software — same parts. Today = the map. |
| 3 | What is SE | Coding (1 script, 1 person) vs engineering (teams, products, years). |
| 4 | Restaurant analogy | The anchor metaphor — keep referring back to it all session. |
| 5 | Client & Server | Ask: "where does Instagram *run* — your phone or somewhere else?" Both! |
| 6 | Frontend | Point out: *this slide* is HTML + CSS. We'll use Streamlit (Python). |
| 7 | Backend | "You never see it, but it's in charge." Logic, security, data. |
| 8 | API | ⭐ Most important for them — calling AI = calling an API. Groq on Day 9. |
| 9 | Database | SQL vs NoSQL; tease vector DBs for Phase 2. |
| 10 | Like-a-post lifecycle | Walk all 6 steps slowly — this ties every concept together. |
| 11 | Git & GitHub | "Save game" + teamwork. Their 4 projects will live on GitHub. |
| 12 | Cloud | "Someone else's computer." All free-tier in this course → ₹0. |
| 13 | DevOps | Culture, not a tool. Bridges Dev and Ops. |
| 14 | CI/CD | "Push code → a robot tests & ships it." |
| 15 | **A day in the life** | Jira board: a ticket travels To Do → In Progress → In Review → Done (branch → PR → CI → deploy). Ties Git/CI/CD/cloud into one real workflow. |
| 16 | Full map (dark) | The payoff slide — every box connected. |
| 17 | Team roles | Career framing; "AI Engineer sits on top of the whole stack." |
| 18 | Where AI fits | Map each course tool onto a box from the talk. |
| 19 | 45-day journey | The 4 phases + "4 deployed projects." Motivation. |
| 20 | Takeaways | "Recognize, don't memorize." |
| 21 | Close | Transition → Module 01: Running Python. Take questions. |

**Theme:** Softpro brand — orange `#E8590C`, cream `#FBF1E6`, white slides, warm dark-grey
`#2B2926`. Type set in **Plus Jakarta Sans** (code in JetBrains Mono). Topic accents stay distinct
(terracotta, gold, brown, steel, olive) but all sit in the warm brand family. Polished with card
hover-lift, staggered content entrance animations, a gradient-mesh cover, and glassy nav controls.

## Editing
All content and styling are inline in `index.html`. To add a slide, copy any
`<section class="slide">…</section>` block; the counter and progress bar update automatically.
Topic accent colors are CSS variables at the top (`--frontend`, `--backend`, …).

➡ After the talk, begin: [01-running-python](../01-running-python/)
