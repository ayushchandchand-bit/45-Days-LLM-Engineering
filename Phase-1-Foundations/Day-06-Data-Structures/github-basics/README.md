# GitHub Basics · Day 6 — Branching & Collaboration (Part 3 of 3)

The finale of the **3-part GitHub mini-track** (Days 4–6). Parts 1–2 covered the *why* and the solo
loop (`add`/`commit`/`push`). Today: how **teams** work together — **branches**, **merges**, **merge
conflicts**, **pull requests**, and **forks** — plus tying the repo back to the Career track (your
GitHub *is* your portfolio).

> Arc: **Day 4 — Why &amp; What** → **Day 5 — The Everyday Workflow** → **Day 6 — Branching &amp;
> Collaboration** (this deck).

## How to present it
Self-contained `index.html` (no install). The centerpiece is an **inline-SVG branch-and-merge graph**;
there's also a PR-flow strip and dark terminal command blocks.
1. Double-click **`index.html`** → press **F** for fullscreen.
2. **→ / Space / click-right** = next · **← / click-left** = back · **Home/End** = jump.

~20 min. Best delivered after students have pushed at least once (Day 5 action done).

## Slide flow + speaker notes
13 slides.

| # | Slide | Talk about / ask the room |
|--:|-------|---------------------------|
| 1 | Title | "The piece that turns a solo skill into a team skill — and an open-source résumé." |
| 2 | The problem | ⭐ "Five people typing in one live doc." The fear of breaking the working version. Branches remove that fear. |
| 3 | What is a branch | **`main` = published book; a branch = a working draft.** Edit the draft, merge when good. |
| 4 | Branch &amp; merge SVG | ⭐ The centerpiece. Trace it: commit → branch off → two feature commits → **merge commit**. Stress `main` was never at risk. |
| 5 | Branch commands | `git switch -c`, normal loop on the branch, `push -u`. Switching branches doesn't touch the others. |
| 6 | Merging | `switch main` then `merge feature`. Note: on GitHub you usually click "Merge", not type it. |
| 7 | Merge conflicts | Defuse the fear. Show the `<<<< ==== >>>>` markers; "Git is just asking you to choose." Edit, remove markers, commit. |
| 8 | Pull Requests + flow | The heart of GitHub. Walk the 6-step strip. "Merged PRs are a real hiring signal." |
| 9 | Fork → branch → PR | Open source. Even one merged PR to a real project is portfolio gold. |
| 10 | Team workflow | The full loop, top to bottom. "This runs at basically every company." |
| 11 | Repo as portfolio | ⭐ Career tie-in: README, green graph, pinned projects, visible PRs. |
| 12 | **GitHub Action** | In-session: branch → push → open a PR → self-merge. First PR is the milestone. |
| 13 | Close | Recap all 3 parts. "From now on, every project lives on GitHub." |

## Teaching tips
- **The SVG (slide 4) does the heavy lifting** — narrate it slowly, left to right. If you have a
  projector, then show the same shape live via the "Insights → Network" graph on a real GitHub repo.
- **Demystify conflicts (slide 7).** Beginners dread them. Frame it as "Git can't read your mind, so
  it asks." Resolve one live if you can — it's anticlimactic in a good way.
- **PRs are the payoff.** This is what "collaborating on GitHub" actually means to employers. Have
  them self-merge their own PR today so the mechanic is concrete, even solo.
- **Keep it conceptual where needed.** A solo learner won't do real code review yet — that's fine.
  The goal is recognising the workflow so they're ready when they join a team or contribute to OSS.
- **Loop back to the Career track** (slide 11): daily commits + a strong README turn coursework into
  a portfolio. This is the same "build in public" thesis, applied to code.

## Today's GitHub Action
On the course repo: `git switch -c add-data-structures` → add Day-6 work → push → **open your first
Pull Request** on github.com → merge it. Bonus: write/upgrade the repo `README.md`. ≤15 min.

## Editing
All inline in `index.html` (shared Softpro template + `.cmd` blocks, `.diagram` SVG wrapper, and a
`.flow` step-strip for the PR pipeline). Copy any `<section class="slide">…</section>` to add a slide.

➡ This completes the GitHub mini-track. From here, every course project is committed and pushed.
