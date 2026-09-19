# Arrays and Hashing

## Sorting algorithms

**Selection sort** — [selection-sort.py](../solutions/arrays-hashing/selection-sort.py)
- For position `q`, find the minimum of `arr[q:]` and swap it into `q`.
- Always O(n²) comparisons, at most n-1 swaps. Not stable.

**Bubble sort** — [bubble-sort.py](../solutions/arrays-hashing/bubble-sort.py), [recursive-bubble-sort.py](../solutions/recursion/recursive-bubble-sort.py)
- Swap adjacent pairs; after pass `p`, the `p` largest values are in place.
- Early exit: reset the "swapped" flag at the start of every pass. In the iterative version the flag is set once and never reset, so the exit only fires when pass 1 makes no swaps. It still sorts, but the O(n) best case is lost.
- The recursive version replaces the outer loop with a call; "no swaps this pass" is the base case.

**Insertion sort** — [insertion-sort.py](../solutions/arrays-hashing/insertion-sort.py), [recursive-insertion-sort.py](../solutions/recursion/recursive-insertion-sort.py)
- Keep `arr[:x]` sorted. Walk `arr[x]` left while it is smaller than its left neighbour; `break` at the first neighbour that isn't larger.
- O(n) on sorted input, stable, the best simple sort for nearly-sorted data.

**Merge sort** — [merge-sort.py](../solutions/arrays-hashing/merge-sort.py)
- Split, sort each half, merge with two pointers, then `extend` whichever tail is left over. O(n log n) always, O(n) extra space.
- **Re-test:** base case must be `len(arr) <= 1`. With `== 1`, an empty list recurses forever.
- **Re-test:** for stability, on a tie take from the LEFT half (`left[i] <= right[j]`). The merge here takes from the right on ties, so equal elements swap places. Harmless for plain ints, wrong when sorting records by a key.

**Quick sort** — [quick-sort.py](../solutions/arrays-hashing/quick-sort.py)
- Partition around a pivot so it lands in its final position, then recurse on each side.
- **Re-test:** the two inner scans need bounds (`left <= right`). Without them the pointer walks off the array: `[1, -3, -4]` raises `IndexError`.
- Average O(n log n). Worst case O(n²) when the pivot is always the smallest or largest, e.g. sorted input with a first-element pivot. In place, not stable.

## Simple scans

**Find max / is sorted / union** — [find-max.py](../solutions/arrays-hashing/find-max.py), [is-sorted-check.py](../solutions/arrays-hashing/is-sorted-check.py), [union-of-two-arrays.py](../solutions/arrays-hashing/union-of-two-arrays.py)
- Start the max at `-inf`, not 0, so all-negative arrays work.
- "Sorted" means non-decreasing: fail only on `arr[i] > arr[i+1]`, so equal neighbours are fine.
- Union: `sorted(set(a) | set(b))`. The [hashmap version](../solutions/arrays-hashing/union-of-two-arrays-hashmap.py) returns keys in insertion order, which is not sorted unless the inputs were.

**Second largest / smallest in one pass** — [second-largest-smallest.py](../solutions/arrays-hashing/second-largest-smallest.py)
- Track two values. When a new maximum arrives, the old maximum becomes the runner-up; also update the runner-up when a value falls strictly between the two.
- Use strict comparisons so a value equal to the max doesn't become the "second" one.

**Leaders in an array** — [leaders-in-array-clean.py](../solutions/arrays-hashing/leaders-in-array-clean.py)
- Scan from the right, keep `maxSoFar`, keep an element only if it is strictly greater; reverse at the end. O(n).
- The [first version](../solutions/arrays-hashing/leaders-in-array.py) is correct but its inner loop is redundant: `result` is increasing, so only the last comparison matters.

**Remove duplicates, keep first-seen order** — [remove-duplicates-unordered.py](../solutions/arrays-hashing/remove-duplicates-unordered.py)
- Seen-set/dict plus a result list. One-liner: `list(dict.fromkeys(arr))`.

**Rotate an array** — [rotate-array-left-by-one.py](../solutions/arrays-hashing/rotate-array-left-by-one.py), [rotate-array-left-by-k.py](../solutions/arrays-hashing/rotate-array-left-by-k.py)
- Always `k %= n` first.
- **Re-test:** in the rotate-right block, `arr[-k:]` with `k == 0` is the WHOLE array, not an empty slice. That doubles the array when `k % n == 0`.

**Missing / repeating numbers** — [find-missing-number.py](../solutions/arrays-hashing/find-missing-number.py), [find-repeating-and-missing.py](../solutions/arrays-hashing/find-repeating-and-missing.py)
- Missing number: the array has N-1 values from 1..N, so the missing value can be N itself.
- **Re-test:** loop to N inclusive (`len(arr) + 1`); stopping at `len(arr)` reports "everything present" when N is the one missing.
- Repeating + missing: with `s1 = sum(arr) - sum(1..n) = rep - miss` and `s2 = sumsq(arr) - sumsq(1..n) = rep² - miss²`, you get `rep + miss = s2 / s1`, then solve the two equations. In Java/C++ use `long`.

**Max consecutive ones** — [max-consecutive-ones.py](../solutions/arrays-hashing/max-consecutive-ones.py)
- `cur = cur + 1 if x == 1 else 0; best = max(best, cur)`.
- **Re-test:** comparing neighbours for equality also counts runs of zeros: `[0,0,0,0]` gives 4.

**Single non-repeating element** — [single-non-repeating-element.py](../solutions/arrays-hashing/single-non-repeating-element.py)
- Count with a dict, return the key with count 1. Know the O(1)-space alternative: XOR everything (`a ^ a = 0`).

## Hashmaps

**Frequency count** — [frequency-count.py](../solutions/arrays-hashing/frequency-count.py)
- `d[x] = d.get(x, 0) + 1`, or `Counter(arr)`.

**Most frequent, with ties** — [most-frequent-with-ties.py](../solutions/arrays-hashing/most-frequent-with-ties.py)
- Keep the best count and every key that reaches it; clear the set when a strictly higher count appears.

**Majority element** — [majority-element.py](../solutions/arrays-hashing/majority-element.py)
- Majority means count strictly greater than `n // 2`, and at most one element can qualify.
- **Re-test:** `>=` prints non-majority values: `[1,1,1,1,2,3,4,5,6]` prints 1 (4 of 9). Know Boyer-Moore voting for the O(1)-space version.

**Longest consecutive sequence** — [longest-consecutive-sequence.py](../solutions/arrays-hashing/longest-consecutive-sequence.py)
- Put everything in a set and only start counting from `x` when `x - 1` is NOT in the set. That makes it O(n).
- The current version starts from every element, so a run of n consecutive numbers costs O(n²).

## Prefix sums and running values

**Longest subarray with sum 0** — [longest-subarray-sum-zero.py](../solutions/arrays-hashing/longest-subarray-sum-zero.py), [v2](../solutions/arrays-hashing/longest-subarray-sum-zero-v2.py)
- Prefix sum + dict of the FIRST index each prefix was seen. Same prefix again means the stretch between is zero. Seed with `{0: -1}`, and never overwrite an existing entry (first index gives the longest).
- The two versions differ on "no such subarray": v1 returns 0, v2 returns -1. Check what the problem wants.
- Works with negatives, unlike a sliding window.

**Maximum subarray sum (Kadane)** — [max-subarray-sum-kadane.py](../solutions/arrays-hashing/max-subarray-sum-kadane.py)
- Drop the running sum when it is <= 0, then add the current value. Start `best` at `-inf` so all-negative arrays work (this version does).

**Maximum product subarray** — [max-product-subarray.py](../solutions/arrays-hashing/max-product-subarray.py)
- Track both the max AND the min product ending here, because a negative times the min becomes the new max. Zero resets both.

## Rearranging in place

**Sort 0/1/2** — [sort-012.py](../solutions/arrays-hashing/sort-012.py) (counting), [sort-012-dutch-flag.py](../solutions/arrays-hashing/sort-012-dutch-flag.py)
- Counting: two passes, simplest, O(n).
- Dutch National Flag, one pass with `low / mid / high`. Invariant: `[0,low)` zeros, `[low,mid)` ones, `(high,end]` twos.
  - see 0: swap(low, mid); `low++`; `mid++`
  - see 1: `mid++`
  - see 2: swap(mid, high); `high--` (do NOT move `mid`, the swapped-in value is unchecked)
- **Re-test:** the current version forgets `mid++` in the 0 case, which breaks as soon as `low == mid`: `[0,0,1,0,2]` raises `IndexError`.

**Rearrange by sign** — [rearrange-by-sign-two-lists.py](../solutions/arrays-hashing/rearrange-by-sign-two-lists.py), [rearrange-by-sign.py](../solutions/arrays-hashing/rearrange-by-sign.py)
- O(n): split into positives and negatives (order kept) and interleave, positives at even indices. Or write straight into a new array with two indices stepping by 2.
- **Re-test:** the in-place shifting version only handles inputs shaped like `[+,+,+,-,-,-]`. Otherwise it overwrites a value and duplicates another.

**Next permutation** — [next-permutation.py](../solutions/arrays-hashing/next-permutation.py)
1. Find the rightmost `i` with `a[i] < a[i+1]` (the pivot).
2. Swap it with the rightmost element greater than `a[i]`.
3. Reverse everything after `i`.
- No pivot means the array is the last permutation: reverse the whole array to wrap around. Handles duplicates.
