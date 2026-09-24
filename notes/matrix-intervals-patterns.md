# Matrix, Intervals and Pattern Printing

## Matrix

**Row with maximum ones** — unsorted rows: [row-with-max-ones.py](../solutions/matrix/row-with-max-ones.py); sorted rows: [row-with-max-ones-sorted-binary-search.py](../solutions/matrix/row-with-max-ones-sorted-binary-search.py)
- Check what the problem guarantees before reaching for a trick. If rows are NOT guaranteed sorted (e.g. `[[0,1],[1,0]]` is valid input), there is no better way than scanning every cell: O(m×n).
- If every row IS guaranteed sorted with 0s before 1s (a stricter, different version — the GfG-style one), binary search each row for the first `1` (that's `lower_bound(row, 1)`); ones in that row = `n - index`. O(m log n).
- Ties go to the row with the smaller index: use a strict `>` when updating the best count, not `>=`. All-zero matrix: no row has a 1, so return -1.

**Search a 2D matrix** — [search-2d-matrix.py](../solutions/matrix/search-2d-matrix.py)
- Applies when the matrix is fully sorted if read left-to-right, top-to-bottom (every row's last value < next row's first value). First binary search the ROWS using `matrix[mid][0]` and `matrix[mid][-1]` to find the row that could contain `target`, then binary search WITHIN that row. O(log rows + log cols).
- Equivalent one-search trick: treat the whole matrix as one flat sorted array of length `rows*cols` and binary search it directly, converting `mid` to `(mid // cols, mid % cols)`.
- Different from Search 2D Matrix II below, which is sorted per-row AND per-column but NOT fully sorted end-to-end — that one needs a different algorithm.

**Search a 2D matrix II** — [search-2d-matrix-ii.py](../solutions/matrix/search-2d-matrix-ii.py)
- Each row is sorted left to right, each column top to bottom, but the matrix is NOT fully sorted end-to-end (row-then-column binary search from the problem above does not apply).
- Start at the top-right corner. That cell is the largest in its row and smallest in its column, so the comparison is unambiguous: too big -> move left (`col -= 1`); too small -> move down (`row += 1`); equal -> found. O(rows + cols).
- Starting at the top-left or bottom-right corner doesn't work: at top-left, "too big" doesn't tell you whether to move right or down.

**Find peak element II** — [find-peak-element-ii.py](../solutions/binary-search/find-peak-element-ii.py)
- A peak is strictly greater than all its (up to four) neighbours; adjacent cells are never equal. Binary search on the COLUMNS: take the middle column, find its maximum cell, and compare that cell with its left and right neighbours in the same row. If a neighbour is larger, move toward it (`high = mid - 1` or `low = mid + 1`); otherwise the cell is a peak. O(rows × log cols).
- Why it works: the max of a column already beats its up/down neighbours, and a larger side neighbour means a peak must exist on that side (the search can only climb, and the edges act like -infinity), same argument as 1D peak finding.
- **Re-test:** the code starts `max1 = 0`, so it only works when every value is >= 1 (true for the LeetCode constraints). With zero or negative values no cell beats 0, and `[[-1,-3]]` returns `[-1,-1]`. Start from the first cell of the column (or `-inf`) instead.
- The line `max = 0` is unused and shadows Python's built-in `max`.

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
