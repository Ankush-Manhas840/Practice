# Strings

## Depth counting

**Remove outermost parentheses** — [remove-outer-parentheses.py](../solutions/strings/remove-outer-parentheses.py)
- A "primitive" is a balanced piece that returns to depth 0 for the first time. The job is to drop the first `(` and last `)` of every primitive.
- Keep a depth counter. For `(`: keep it only if the depth is already >= 1, then increment. For `)`: keep it only if the depth is > 1, then decrement. Check first, update second; swapping the order shifts everything by one.
- One pass, O(n). Checked against an independent reference on 607 random balanced strings, including the empty string.
- The same depth-counter idea solves "maximum nesting depth" and is the base of the valid-parentheses checks you'll meet next.

## Habits worth fixing

- **Don't name a variable `str`.** It shadows Python's built-in `str` inside that scope; it works here only because nothing calls `str(...)` afterwards. The same happened with `max`, `sum` and `min` in earlier solutions (`find-max`, `max-subarray-sum-kadane`, `four-sum`, `longest-subarray-sum-k`). Use `result`, `total`, `best`, and so on.
- **Building a string with `+=` in a loop:** CPython often optimizes it, but it is not guaranteed and can be O(n²) in other cases. Collect pieces in a list and `"".join(pieces)` at the end for a guaranteed O(n).
