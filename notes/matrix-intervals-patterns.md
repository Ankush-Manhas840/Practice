# Matrix, Intervals and Pattern Printing

## Matrix

**Row with maximum ones** — [row-with-max-ones.py](../solutions/matrix/row-with-max-ones.py)
- Check what the problem guarantees before reaching for a trick. If rows are NOT guaranteed sorted (e.g. `[[0,1],[1,0]]` is valid input), there is no better way than scanning every cell: O(m×n). Binary search per row (find the first `1` in each row) only works when a row is guaranteed sorted with 0s before 1s — a stricter, different version of this problem. Don't assume the sorted variant just because the title sounds familiar.
- Ties go to the row with the smaller index: use a strict `>` when updating the best count, not `>=`.

**Set matrix zeroes** — [set-matrix-zeroes.py](../solutions/matrix/set-matrix-zeroes.py)
- Record the coordinates of every zero FIRST, then zero their rows and columns. Zeroing while you scan turns the new zeros into more zeros.
- Extra memory is O(number of zeros). The O(1)-space version uses the first row and first column as the markers.

**Rotate 90° clockwise** — [rotate-matrix-90.py](../solutions/matrix/rotate-matrix-90.py)
- Transpose (swap `[i][j]` with `[j][i]` only where `i < j`), then reverse each row. For counter-clockwise, transpose and then reverse the order of the rows (flip top to bottom) instead.
- Square matrices only: a 2x3 input raises `IndexError`.

**Spiral traversal** — [spiral-matrix-traversal.py](../solutions/matrix/spiral-matrix-traversal.py)
- Keep four boundaries `top, bottom, left, right`. Walk the top row, then the right column, then (guard) the bottom row, then (guard) the left column, and shrink each boundary after using it.
- The guards are the important part: `if top <= bottom` before the bottom row and `if left < right` before the left column. Without them, a single row or single column gets printed twice. This version passed 300 random rectangles.

## Intervals

**Merge overlapping intervals** — [merge-intervals.py](../solutions/intervals/merge-intervals.py)
- Sort by start. For each interval: if it starts at or before the last merged interval's end, merge (`end = max(end, new_end)`); otherwise append it.
- **Re-test:** intervals that only touch, `[1,3]` and `[3,5]`, count as overlapping in the standard problem and should become `[1,5]`. The current version compares with `last_end <= new_start` to decide "separate", so touching intervals stay apart.

## Pattern printing

Solutions: [patterns-batch-1.py](../solutions/pattern-printing/patterns-batch-1.py), [concentric-number-square.py](../solutions/pattern-printing/concentric-number-square.py)

How to attack any pattern:
1. The outer loop is the row `x`; the inner loops print one row.
2. Find, for row `x`, how many spaces, how many symbols, and what each symbol is.
3. Pyramid of `n` rows: row `x` has `n - x` leading spaces and `2x - 1` stars. A full diamond is the pyramid followed by the pyramid reversed.
4. A diamond written as one loop with a `direction` variable: move the counts one way until the middle row, flip `direction`, then move them back.
5. Hollow shapes: print the symbol only on the border (`x == 1 or x == n or y == 1 or y == n`), a space otherwise.
6. Concentric squares: the value at `(x, y)` is `n - min(distance to top, bottom, left, right)`, which is how [concentric-number-square.py](../solutions/pattern-printing/concentric-number-square.py) works.
7. Letters: `chr(65 + k)` gives `A, B, C...`; `chr(97 + k)` gives lowercase.
8. `print(..., end="")` keeps a row on one line; a bare `print()` ends it.

Gotcha in [patterns-batch-1.py](../solutions/pattern-printing/patterns-batch-1.py) (around line 83): `n = input(...)` returns a string, so `n - 1` raises `TypeError`. Wrap it: `n = int(input(...))`. Running the file as a script stops there.
