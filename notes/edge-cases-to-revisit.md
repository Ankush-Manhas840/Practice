# Edge Cases to Revisit

Result of running each solution against a brute-force checker (random inputs plus hand-picked edge
cases) on 2026-09-19. 79 of the 81 non-pattern solution files were checked; the pattern-printing
files, frequency-count and count-digits were not.

Every entry in the first table produced a wrong answer or a crash on an input that is valid for the
problem. Each one worked on the input it was first written for. To revise: re-solve the problem from a blank
file, then run your version on the failing input.

## Wrong answer or crash

| Solution | Failing input | What goes wrong | Direction for the fix |
|---|---|---|---|
| [move-zeroes-to-end](../solutions/two-pointers/move-zeroes-to-end.py) | `[1,2,0,3]` gives `[1,0,2,3]` | scan pointer `i` overtakes `j` | one write index for the next non-zero slot |
| [majority-element](../solutions/arrays-hashing/majority-element.py) | `[1,1,1,1,2,3,4,5,6]` prints 1 | `>= n//2`, but majority needs `> n//2` | strict comparison |
| [merge-intervals](../solutions/intervals/merge-intervals.py) | `[[1,3],[3,5]]` stays split | touching intervals should merge into `[1,5]` | merge when `new_start <= last_end` |
| [three-sum](../solutions/two-pointers/three-sum.py) | `[-1,0,1,2,-1,-4]` gives `[-1,0,1]` twice | no duplicate skipping | skip repeated `i`; skip repeats after a hit |
| [search-rotated-sorted-array](../solutions/binary-search/search-rotated-sorted-array.py) | `[27,28,1,5,20,24]`, target 27, gives "Not available" | tests the target range before knowing which half is sorted (about 13% of searches fail) | decide the sorted half first, then check the target against it |
| [search-rotated-sorted-array-duplicates](../solutions/binary-search/search-rotated-sorted-array-duplicates.py) | `[1,0,1,1,1]`, target 0, gives False | `arr[low] <= arr[mid]` doesn't prove the left half is sorted when values repeat | if low, mid, high are all equal, shrink both ends |
| [rearrange-by-sign](../solutions/arrays-hashing/rearrange-by-sign.py) (in-place shift) | `[1,-7,-4,2,-6,5,6,-2]` corrupts to `[1,-7,-4,-4,-6,-6,6,-2]` | assumes the next slot holds a positive; only handles `[+,+,+,-,-,-]` shapes | the two-lists version passes |
| [sort-012-dutch-flag](../solutions/arrays-hashing/sort-012-dutch-flag.py) | `[0,0,1,0,2]` raises `IndexError`; `[2,2,1,0,2,0]` wrong | 0 case moves `low` but not `mid` | on 0: swap, `low++`, `mid++` |
| [merge-sort](../solutions/arrays-hashing/merge-sort.py) | `[]` raises `RecursionError` | base case is `len == 1` | `len <= 1` |
| [quick-sort](../solutions/arrays-hashing/quick-sort.py) | `[1,-3,-4]` raises `IndexError` | inner scans have no bounds | bound both scans |
| [find-missing-number](../solutions/arrays-hashing/find-missing-number.py) | `[1..7]` (N=8) prints "Everything is present" | loop stops at `len(arr)`, but the missing value can be N | loop through N inclusive |
| [max-consecutive-ones](../solutions/arrays-hashing/max-consecutive-ones.py) | `[0,0,0,0]` gives 4 | counts runs of any repeated value | `cur = cur+1 if x == 1 else 0` |
| [rotate-array-left-by-k](../solutions/arrays-hashing/rotate-array-left-by-k.py) (rotate-right block) | `[1,2,3,4]`, k=12 gives the array doubled | `arr[-0:]` is the whole array | special-case `k % n == 0` |
| [prime-check](../solutions/math-geometry/prime-check.py) | `1`, `0`, `-1` print "Prime" | no `n < 2` guard | return "not prime" first |
| [pascals-triangle-element-formula](../solutions/math-geometry/pascals-triangle-element-formula.py) | row 12, col 6 gives 461 (should be 462) | float `/` then `int()` truncates | integer `//` at each step |
| [matrix-median](../solutions/binary-search/matrix-median.py) | FIXED 2026-09-24. Before: never finished, even on `[[1,3,5],[2,6,9],[3,6,9]]` | `while low <= high` combined with `high = mid` repeats forever once `low == high` | `high = mid - 1` (or switch to `while low < high`) |
| [median-of-two-sorted-arrays](../solutions/binary-search/median-of-two-sorted-arrays.py) | FIXED 2026-09-21. Before: `[1,3]` and `[2,3]` gave 3.0 (should be 2.5) | the "equal values" branch skipped two positions at once and overwrote `prev` | equal values are now an ordinary single step |

## Quietly assume positive numbers

| Solution | Failing input | Why |
|---|---|---|
| [count-subarrays-sum-k](../solutions/sliding-window/count-subarrays-sum-k.py) | `[1,-1,1]`, k=1 gives 1 (should be 3) | sliding window needs the sum to change monotonically |
| [longest-subarray-sum-k](../solutions/sliding-window/longest-subarray-sum-k.py) | random arrays with negatives raise `IndexError` | same |

For arrays with negatives, use prefix sums + a dict.

| Solution | Failing input | Why |
|---|---|---|
| [max-nesting-depth-parentheses](../solutions/strings/max-nesting-depth-parentheses.py) | `"((("` returns 0 (should be 3) | records the maximum only at a `)`, so it needs a balanced string (which the problem guarantees) |

| Solution | Failing input | Why |
|---|---|---|
| [find-peak-element-ii](../solutions/binary-search/find-peak-element-ii.py) | `[[-1,-3]]` returns `[-1,-1]` | starts `max1 = 0`, so it needs every value >= 1 (true under LeetCode's constraints) |

| Solution | Failing input | Why |
|---|---|---|
| [gas-station-min-max-distance](../solutions/binary-search/gas-station-min-max-distance.py) | `[1,1,5]`, k=1 gives about 1.33 (should be 2) | assumes strictly increasing positions; a zero gap contributes `-1` to the count |

## Correct, but worth knowing

- [find-divisors](../solutions/math-geometry/find-divisors.py): output is interleaved, not sorted (`[1,12,2,6,3,4]` for 12).
- [union-of-two-arrays-hashmap](../solutions/arrays-hashing/union-of-two-arrays-hashmap.py): output is in insertion order, not sorted.
- [rotate-matrix-90](../solutions/matrix/rotate-matrix-90.py): square matrices only.
- [merge-sort](../solutions/arrays-hashing/merge-sort.py): not stable (takes from the right half on ties).
- [bubble-sort](../solutions/arrays-hashing/bubble-sort.py): the early-exit flag is never reset, so the O(n) best case only triggers if pass 1 has no swaps.
- [longest-consecutive-sequence](../solutions/arrays-hashing/longest-consecutive-sequence.py): correct, but O(n²) worst case. Start a run only when `x - 1` is not in the set.
- [leaders-in-array](../solutions/arrays-hashing/leaders-in-array.py) (first version): correct, but the inner loop is redundant.
- [kth-missing-positive-number](../solutions/binary-search/kth-missing-positive-number.py): correct, O(n·(n+k)) because of `in` on a list.
- [kth-missing-positive-number-binary-search](../solutions/binary-search/kth-missing-positive-number-binary-search.py): correct, but relies on Python's negative indexing when `high` ends at -1.
- [koko-eating-bananas](../solutions/binary-search/koko-eating-bananas.py): unused `test = piles[:]` inside the loop.
- [fibonacci-recursive](../solutions/recursion/fibonacci-recursive.py): uses `fibo(0) = fibo(1) = 1`, shifted from the textbook sequence.
- [patterns-batch-1.py](../solutions/pattern-printing/patterns-batch-1.py): `n = input(...)` is a string, so `n - 1` raises `TypeError`.

## Checked and fine

All of these matched the brute force on every random input tried:

- Sorting: selection, bubble, insertion, recursive bubble, recursive insertion, merge sort (non-empty lists).
- Arrays: Kadane, max product subarray, find-repeating-and-missing, leaders (both versions), longest subarray with sum zero (both), longest consecutive, sort-012 (counting version), next permutation, rotate-left-by-one and rotate-left-by-k (left block).
- Two pointers and windows: four-sum, remove-duplicates-sorted-array, merge-sorted-arrays-inplace, reverse (iterative and recursive), best time to buy and sell, longest-subarray-sum-k (positives only).
- Matrix: set matrix zeroes, spiral, rotate matrix (square).
- Binary search: plain search, lower/upper bound, floor/ceil, last occurrence, count occurrences, search insert position, find min in a rotated array, rotation count, single non-duplicate, peak element, sqrt, nth root, Koko, bouquets, smallest divisor, ship within days, aggressive cows, both kth-missing versions.
- Math and recursion: palindrome number, Armstrong, gcd, find-divisors (as a set), row-building Pascal, recursive palindrome, factorial.
