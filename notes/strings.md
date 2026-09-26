# Strings

## Depth counting

**Remove outermost parentheses** — [remove-outer-parentheses.py](../solutions/strings/remove-outer-parentheses.py)
- A "primitive" is a balanced piece that returns to depth 0 for the first time. The job is to drop the first `(` and last `)` of every primitive.
- Keep a depth counter. For `(`: keep it only if the depth is already >= 1, then increment. For `)`: keep it only if the depth is > 1, then decrement. Check first, update second; swapping the order shifts everything by one.
- One pass, O(n). Checked against an independent reference on 607 random balanced strings, including the empty string.
- The same depth-counter idea solves "maximum nesting depth" (next entry) and is the base of the valid-parentheses checks you'll meet next.

**Maximum nesting depth** — [max-nesting-depth-parentheses.py](../solutions/strings/max-nesting-depth-parentheses.py)
- Depth counter again: `(` adds one, `)` subtracts one, the answer is the largest value the counter reaches. Other characters (digits, `+`, `*`) are simply ignored. O(n), O(1) space.
- Checked on 607 random valid strings with digits and operators mixed in.
- The code records the maximum when it sees a `)`, just before decrementing. That is correct because the problem guarantees a balanced string, but on an unbalanced input like `"((("` it returns 0 instead of 3. Recording the maximum right after incrementing on `(` works for both.
- Same lesson as elsewhere: know what the problem guarantees, and know which of those guarantees your code silently relies on.

## Lookup tables and comparing neighbours

**Roman to integer** — [roman-to-integer.py](../solutions/strings/roman-to-integer.py)
- Read left to right. A smaller value written before a larger one (`IV`, `IX`, `XC`, `CM`) is subtracted; otherwise it is added.
- Your version works one step behind: on each new character it adds or subtracts the PREVIOUS value depending on whether it is smaller than the current one, then adds the last value after the loop. Checked against every valid numeral from 1 to 3999.
- A dictionary (`{'I': 1, 'V': 5, ...}`) replaces the long `if/elif` chain in `val` and returns a clear `KeyError` for a bad character.
- Anything that isn't an uppercase Roman letter makes `val` return `None`, and the comparison then raises a `TypeError` (`"iv"` and `"XZ"` both do). The problem guarantees valid input, so this is fine here.

## Expanding from a centre

**Longest palindromic substring** — [longest-palindromic-substring.py](../solutions/strings/longest-palindromic-substring.py)
- Every palindrome has a centre, so try each one and grow outward while the two ends match. There are `2n - 1` centres: `n` on a single character (odd length) and `n - 1` between two characters (even length). Skipping the even case is the classic mistake, and it would miss `"bb"` in `"cbbd"`.
- When the loop stops, the palindrome is `s[left + 1 : right]`, because `left` and `right` have already stepped one past the last matching pair.
- O(n²) time, O(1) extra space. Checked on 2,800+ inputs, including every binary string up to length 10.
- Ties: it keeps the first longest one it finds (`"babad"` gives `"bab"`), and the problem accepts any longest palindrome. The `<` in `len(lon) < len(cand)` is what keeps the earlier one.
- Worth knowing for later: Manacher's algorithm does the same job in O(n), and a DP table over `(i, j)` is the O(n²)-space version you'll see in editorials.

## Counting inside substrings

**Sum of beauty of all substrings** — [sum-of-beauty-of-all-substrings.py](../solutions/strings/sum-of-beauty-of-all-substrings.py)
- Beauty of a substring is (highest letter count) minus (lowest letter count). Fix the start `i`, extend the end `j` one letter at a time, update the counts incrementally, and add the beauty of each new substring. Never recount a substring from scratch.
- The repo version is the intended approach: O(n²) substrings, with an O(26) max/min scan on each. The problem's limit of n <= 500 is sized for exactly this. Checked on 909 inputs against a brute force.
- No asymptotically better algorithm is known or expected for this problem, so "no better solution" is roughly right. But the 26 factor can be removed, and it is a real speed-up (0.07s instead of 0.77s on a 500-letter string):
  - The max only ever goes up as you extend, so `maxf = max(maxf, cnt[c])`.
  - For the min, keep `freq[k]` = how many letters currently have count `k`. When a letter's count goes from `old` to `old + 1`: a brand-new letter sets `minf = 1`; otherwise if `old == minf` and `freq[old]` is now 0, then `minf += 1`.
  - That is O(1) per step, so O(n²) overall.
- Worth learning: the incremental-count pattern (that is the point of the problem) and using a 26-slot array instead of a dict for lowercase letters. The frequency-of-frequencies table is a small trick that comes back in some harder problems, so ten minutes on it is plenty.
- Small style notes: `max(hashmap.values())` is simpler than `max(hashmap, key=hashmap.get)` followed by a lookup, and `sum` shadows the built-in again.

## Parsing rules

**String to integer (atoi)** — [string-to-integer-atoi.py](../solutions/strings/string-to-integer-atoi.py)
- Follow the rules in order: skip leading spaces, read one optional sign, read digits until the first non-digit, then clamp to `[-2^31, 2^31 - 1]`. Anything after the digits is ignored (`"3.14"` gives 3, `"1337c0d3"` gives 1337).
- The trap is a sign followed by no digits (`"+"`, `"-"`, `"+-12"`, `"- 5"`): the answer is 0. Comparing where the sign ended (`j`) with where the digits ended (`i`) is what handles it. `"words and 987"` is also 0, because parsing stops at the first character.
- Python integers don't overflow, so you can build the full number and clamp once at the end. In Java or C++ you must check for overflow before each `x = x * 10 + digit`.
- Checked against a reference on 22,026 inputs, including values right at the 32-bit limits.
- `s.lstrip()` strips tabs and newlines as well as spaces; the problem only counts the space character. So `"\t42"` returns 42 here, where the strict rule says 0. Tabs can't occur in this problem's inputs, but it is the kind of difference that matters when an interviewer changes the spec.

## Habits worth fixing

- **Don't name a variable `str`.** It shadows Python's built-in `str` inside that scope; it works here only because nothing calls `str(...)` afterwards. The same happened with `max`, `sum` and `min` in earlier solutions (`find-max`, `max-subarray-sum-kadane`, `four-sum`, `longest-subarray-sum-k`). Use `result`, `total`, `best`, and so on.
- **Building a string with `+=` in a loop:** CPython often optimizes it, but it is not guaranteed and can be O(n²) in other cases. Collect pieces in a list and `"".join(pieces)` at the end for a guaranteed O(n).
