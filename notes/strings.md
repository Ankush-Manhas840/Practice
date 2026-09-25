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

## Habits worth fixing

- **Don't name a variable `str`.** It shadows Python's built-in `str` inside that scope; it works here only because nothing calls `str(...)` afterwards. The same happened with `max`, `sum` and `min` in earlier solutions (`find-max`, `max-subarray-sum-kadane`, `four-sum`, `longest-subarray-sum-k`). Use `result`, `total`, `best`, and so on.
- **Building a string with `+=` in a loop:** CPython often optimizes it, but it is not guaranteed and can be O(n²) in other cases. Collect pieces in a list and `"".join(pieces)` at the end for a guaranteed O(n).
