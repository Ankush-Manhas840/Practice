# Two Pointers and Sliding Window

## Two pointers on arrays

**Reverse in place** — [reverse-array-iterative.py](../solutions/two-pointers/reverse-array-iterative.py)
- Swap the ends and move inward; stop when the pointers meet. The current version indexes with `-j` from the back, which is the same idea.

**Remove duplicates from a sorted array** — [remove-duplicates-sorted-array.py](../solutions/two-pointers/remove-duplicates-sorted-array.py)
- Slow pointer = where the next unique value goes; fast pointer scans. Write when `arr[fast] != arr[slow-1]`. Return the count, and the answer is `arr[:count]`.

**Move zeroes to the end** — [move-zeroes-to-end.py](../solutions/two-pointers/move-zeroes-to-end.py)
- One write index for the next non-zero slot. Scan with a second index and, on each non-zero, swap it into the write slot and advance the write index. This keeps the non-zero order.
- **Re-test:** the current version moves both pointers around and lets `i` overtake `j`. `[1,2,0,3]` comes out as `[1,0,2,3]`.

**Merge two sorted arrays in place** — [merge-sorted-arrays-inplace.py](../solutions/two-pointers/merge-sorted-arrays-inplace.py)
- Fill from the back with the largest value first, so nothing you still need is overwritten. Verified against random inputs.

## Sort first, then two pointers

**3Sum** — [three-sum.py](../solutions/two-pointers/three-sum.py)
- Sort. Fix `i`, then move `left` and `right` inward: sum too big, move `right`; too small, move `left`.
- Sorting is what makes the pointer moves valid.
- **Re-test:** duplicates. Skip repeated values of `i`, and after finding a triplet advance `left`/`right` past repeats. Without that, `[-1,0,1,2,-1,-4]` reports `[-1,0,1]` twice.

**4Sum** — [four-sum.py](../solutions/two-pointers/four-sum.py)
- Same idea with two fixed indices. The `not in result` check removes duplicates and passed random tests with many repeats; the standard approach skips duplicates instead, which avoids the list scan.

## Sliding window

**Best time to buy and sell stock** — [best-time-to-buy-sell-stock.py](../solutions/sliding-window/best-time-to-buy-sell-stock.py)
- One pass: keep the minimum price so far, `profit = max(profit, price - min)`. Answer is 0 when prices only fall.

**Subarray sum equal to k, positives only** — [longest-subarray-sum-k.py](../solutions/sliding-window/longest-subarray-sum-k.py), [count-subarrays-sum-k.py](../solutions/sliding-window/count-subarrays-sum-k.py)
- Grow the window on the right; while the sum exceeds `k`, shrink from the left; record when it equals `k`.
- This only works when every number is positive, because that makes the sum rise and fall predictably as the window grows and shrinks.
- **Re-test:** with negatives or zeros it breaks. `[1,-1,1]`, `k=1` counts 1 instead of 3, and random arrays with negatives can raise `IndexError`.
- For arrays that can contain negatives use prefix sums + a dict: at each index add `freq[prefix - k]` to the count, then record the prefix. Same idea as [longest-subarray-sum-zero.py](../solutions/arrays-hashing/longest-subarray-sum-zero.py).
