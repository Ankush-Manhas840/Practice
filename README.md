# DSA Practice

A tracked, spaced-repetition DSA practice system. Claude generates a daily set,
you solve it, Claude logs it and schedules the review.

## Layout

```
practice/
  progress.json      <- source of truth: every question, its status, next review date
  daily/              <- one file per day, e.g. daily/2026-07-27.md, with that day's set
  solutions/<topic>/  <- your solutions, e.g. solutions/arrays-hashing/two-sum.py
  README.md
```

## How the daily set works

Each day's set is a mix (per your preference):
- **Review questions**: anything in `progress.json` whose `next_review` date has arrived,
  pulled from what you've already attempted.
- **New questions**: 1-2 fresh problems, biased toward topics with the fewest entries so far
  (see `topics` list in `progress.json`).

## Spaced repetition rule

Each question has an `interval_index` into `review_intervals_days: [1, 3, 7, 14, 30, 60]`.

- Solve it cleanly on review -> `interval_index` moves up one (next review further away).
- Struggle or fail -> `interval_index` resets to `0` (review again tomorrow).
- A question "graduates" (stops appearing) after it's been solved cleanly at the last interval (60 days).

## Daily workflow

1. Each morning a scheduled task writes `daily/<date>.md` with that day's questions.
2. You solve them, saving code under `solutions/<topic>/<id>.py`.
3. Tell Claude you're done (or paste your solution / say where you got stuck).
4. Claude updates `progress.json` (status, next review date) and commits locally.
5. Claude will **always ask before pushing to GitHub** — nothing goes to the public
   repo without your explicit go-ahead each time, unless you tell it to stop asking.

## Question entry schema (progress.json)

```json
{
  "id": "two-sum",
  "title": "Two Sum",
  "topic": "arrays-hashing",
  "difficulty": "Easy",
  "first_attempted": "2026-07-27",
  "status": "new | solved | struggled",
  "interval_index": 0,
  "times_reviewed": 0,
  "last_reviewed": "2026-07-27",
  "next_review": "2026-07-28",
  "solution_file": "solutions/arrays-hashing/two-sum.py"
}
```
