# Binary Search

## The template

```python
low, high = 0, len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target: ...      # found
    elif arr[mid] < target: low = mid + 1
    else: high = mid - 1
```

- Loop on `low <= high`. With `low < high` the last remaining candidate is never checked, so a target sitting at the final position is missed. This was fixed in [binary-search.py](../solutions/binary-search/binary-search.py).
- Always move past `mid` (`mid + 1` / `mid - 1`), otherwise the loop can spin forever.
- "First index where a condition holds": when the condition is true, record `result = mid` and keep searching left (`high = mid - 1`). When it's false, go right.
- After the loop ends with `low > high`, `low` is the insertion point.

## Boundaries and counting

**Lower bound / upper bound** — [lower-bound.py](../solutions/binary-search/lower-bound.py), [upper-bound.py](../solutions/binary-search/upper-bound.py)
- Lower bound: first index with `arr[i] >= x` (`bisect_left`). Upper bound: first index with `arr[i] > x` (`bisect_right`). Both default to `n` when nothing qualifies.
- The only difference is `>=` versus `>` in one condition.

**Search insert position** — [search-insert-position.py](../solutions/binary-search/search-insert-position.py)
- It is a lower bound. `low` at the end is where the target belongs.

**Floor and ceiling** — [floor-ceil-sorted-array.py](../solutions/binary-search/floor-ceil-sorted-array.py)
- Floor = largest value <= x, ceiling = smallest value >= x, -1 when none exists.
- After a failed search `high` sits on the floor and `low` on the ceiling. Guard `high < 0` and `low >= n`.

**First / last occurrence, count** — [last-occurrence.py](../solutions/binary-search/last-occurrence.py), [count-occurrences-sorted-array.py](../solutions/binary-search/count-occurrences-sorted-array.py)
- On a match, record it and keep going: left for the first occurrence, right for the last.
- Count = last - first + 1 (or `upper_bound - lower_bound`).

## Rotated sorted arrays

**Search in a rotated array** — [search-rotated-sorted-array.py](../solutions/binary-search/search-rotated-sorted-array.py)
- At every step at least one half is sorted. Decide WHICH half first (`arr[low] <= arr[mid]` means the left half is sorted), then check whether the target lies inside that half's range.
- **Re-test:** the current version tests "is the target between `arr[low]` and `arr[mid]`" before knowing which half is sorted. It fails on `[27,28,1,5,20,24]`, target 27 (about 13% of searches in random tests).

**With duplicates** — [search-rotated-sorted-array-duplicates.py](../solutions/binary-search/search-rotated-sorted-array-duplicates.py)
- If `arr[low] == arr[mid] == arr[high]` you cannot tell which half is sorted. Shrink both ends (`low++`, `high--`) and continue. Worst case becomes O(n).
- **Re-test:** without that step, `[1,0,1,1,1]` with target 0 returns False.

**Minimum / rotation count** — [find-minimum-rotated-sorted-array.py](../solutions/binary-search/find-minimum-rotated-sorted-array.py), [find-rotation-count.py](../solutions/binary-search/find-rotation-count.py)
- The minimum is the rotation point. Rotation count = index of the minimum.
- If the left half is sorted, its first element is the best candidate in that half, so record it and go right; otherwise go left. Verified for distinct values.

## Other index tricks

**Single non-duplicate in a sorted array of pairs** — [single-non-duplicate.py](../solutions/binary-search/single-non-duplicate.py)
- Force `mid` to be even. If `arr[mid] == arr[mid+1]`, the pairing is still intact on the left, so the single is on the right (`start = mid + 2`). Otherwise it is at `mid` or left of it (`end = mid`). Loop on `start < end` and return `arr[start]`.

**Peak element** — [find-peak-element.py](../solutions/binary-search/find-peak-element.py)
- If `arr[mid] < arr[mid+1]` a peak exists to the right (`start = mid + 1`), otherwise `mid` or something to its left (`end = mid`). Returns any peak. Works because both ends count as -infinity.

**Kth missing positive** — [kth-missing-positive-number-binary-search.py](../solutions/binary-search/kth-missing-positive-number-binary-search.py), [brute force](../solutions/binary-search/kth-missing-positive-number.py)
- Numbers missing before index `i` = `arr[i] - (i + 1)`. Binary search for where that first reaches `k`; the answer works out to `k + high + 1`.
- When `k` is smaller than the missing count before the first element, `high` ends at -1 and `arr[high]` reads the last element through Python's negative indexing. It cancels out algebraically and stays correct, but it would be out of bounds in Java or C++.
- The brute force is correct but `start not in arr` scans a list every time, so it is O(n·(n+k)).

**Median of two sorted arrays** — [median-of-two-sorted-arrays.py](../solutions/binary-search/median-of-two-sorted-arrays.py)
- The repo version walks both arrays like a merge until it reaches the middle: O(n + m), and no binary search.
- **Re-test:** it breaks when the arrays share a value on the middle positions. The "equal" branch counts two steps at once and overwrites `prev`, so `[1,3]` and `[2,3]` gives 3.0 instead of 2.5. Simply taking one element per step fixes it.
- The O(log(min(n, m))) version is the one to learn: binary search the cut position `i` in the smaller array, which fixes the cut `j = (n + m + 1) // 2 - i` in the other. A cut is valid when `maxLeftA <= minRightB` and `maxLeftB <= minRightA` (use -inf / +inf past the ends). Odd total: the median is `max(maxLeftA, maxLeftB)`; even total: the average of that and `min(minRightA, minRightB)`.

## Binary search on the answer

Use it when you can test "does value `x` work?" and the answers flip exactly once as `x` grows.

1. Define `feasible(x)`; it must be monotonic.
2. Pick the search range from the problem (below).
3. Minimising: if feasible, `ans = mid; high = mid - 1`, else `low = mid + 1`.
4. Maximising: if feasible, `ans = mid; low = mid + 1`, else `high = mid - 1`.

| Problem | Range | feasible(x) |
|---|---|---|
| [Koko eating bananas](../solutions/binary-search/koko-eating-bananas.py) | 1 .. max(piles) | hours needed at speed x <= h |
| [Ship within D days](../solutions/binary-search/ship-within-days.py) | max(weights) .. sum(weights) | days needed with capacity x <= D |
| [Min days for bouquets](../solutions/binary-search/minimum-days-to-make-bouquets.py) | 1 .. max(bloomDay) | bouquets possible on day x >= m |
| [Allocate minimum pages](../solutions/binary-search/allocate-minimum-pages.py) | max(arr) .. sum(arr) | students needed when nobody reads more than x pages <= k |
| [Smallest divisor](../solutions/binary-search/smallest-divisor-threshold.py) | 1 .. max(nums) | sum of ceil(n / x) <= threshold |
| [Aggressive cows](../solutions/binary-search/aggressive-cows.py) (maximise) | 1 .. max - min | cows placeable with gap >= x is >= k |
| [Gas station min-max distance](../solutions/binary-search/gas-station-min-max-distance.py) (real numbers) | 0 .. max(stations) | new stations needed at max gap x, sum of `ceil(gap / x) - 1`, is <= k |
| [Integer sqrt](../solutions/binary-search/sqrt-integer.py) (maximise) | 0 .. x | mid * mid <= x |
| [Nth root](../solutions/binary-search/nth-root.py) | 0 .. m | mid ** n vs m; -1 if never equal |

Details worth remembering:
- Ceiling division: `(a + b - 1) // b` or `-(-a // b)`.
- Ship: the lower bound is `max(weights)` because one package must fit; the upper bound is the total.
- Allocate pages, [Split Array Largest Sum](../solutions/binary-search/split-array-largest-sum.py) and [Painter's Partition](../solutions/binary-search/painters-partition.py) are the same "split an array into k contiguous groups and minimise the largest group sum" problem as Ship, with the same bounds. Once you spot this shape, all four are one solution with different names.
- Painter's Partition with more painters than boards: the extra painters stay idle, so the answer is `max(arr)`. The search handles this without a special case because counting groups with `<= k` always succeeds at `max(arr)`. Return -1 when `k > n`, since every student needs a book. Counting groups with `<= k` is fine: if you can do it with fewer groups you can always split further.
- Bouquets: return -1 up front when `m * k > n`. Reset the streak when a flower isn't ready AND after forming a bouquet.
- Cows: sort first; place greedily at the first stall at least `mid` away from the last cow.
- Koko has an unused `test = piles[:]` copy inside the loop, which is wasted work each iteration.
- Answer is a real number (gas station): you can't step by `mid +/- 1`. Loop `while high - low > 1e-6`, and set `high = mid` when feasible, `low = mid` otherwise. The result is only accurate to that tolerance, so compare with a tolerance, not `==`.
- Gas station: the current version assumes station positions are strictly increasing. A repeated position gives a zero gap, and `ceil(0 / mid) - 1 = -1` lowers the count; `[1,1,5]` with k=1 returns about 1.33 instead of 2. Clamp each gap's contribution at 0 (`max(0, ...)`).
- sqrt / nth root: Python integers don't overflow; in Java/C++ use `long` and compare `mid <= x / mid`.
