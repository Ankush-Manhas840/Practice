# DSA Notes

Revision notes built from the solutions in this repo. One file per topic. Each entry is the
trick worth remembering, plus the places where the solution in this repo needs care.

Last checked against the code: 2026-09-19.

## Files

| File | Covers |
|---|---|
| [arrays-hashing.md](arrays-hashing.md) | sorting algorithms, array scans, hashmaps, prefix sums, Kadane, next permutation |
| [binary-search.md](binary-search.md) | the template, lower/upper bound, rotated arrays, binary search on the answer |
| [two-pointers-sliding-window.md](two-pointers-sliding-window.md) | in-place tricks, 3Sum/4Sum, sliding windows and their limits |
| [recursion-math.md](recursion-math.md) | recursion basics, number theory, Pascal's triangle |
| [matrix-intervals-patterns.md](matrix-intervals-patterns.md) | matrix traversal/rotation, merge intervals, pattern printing |
| [edge-cases-to-revisit.md](edge-cases-to-revisit.md) | every solution that broke on some input, with the failing input |

## How to revise

1. Read one topic file.
2. For each entry with a **Re-test** line, close the notes and re-solve it from a blank file.
3. Run your version through the checklist below before calling it done.

## Edge-case checklist

Run every solution on these before moving on:

- empty input and a single element
- all elements equal, all zeros, all negative
- duplicates
- the answer or target at the first or last position; target absent
- `k = 0`, `k = n`, `k > n`
- already sorted and reverse sorted
- large values (float division, overflow in Java/C++)

## Why the checklist exists

On 2026-09-19 every solution that takes an input and returns an answer (79 of 81 files) was run
against a brute-force checker. 15 gave a wrong answer or crashed on some valid input, and 2 more
quietly assume all numbers are positive. Almost every failure was one of the cases above that the
original test input didn't include. Details in [edge-cases-to-revisit.md](edge-cases-to-revisit.md).
