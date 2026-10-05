# Recursion and Math

## Recursion

Every recursive function needs (1) a base case that returns without recursing and (2) a call on a strictly smaller input. Write the base case first.

**Factorial, with input checking** — [factorial-with-raise.py](../solutions/recursion/factorial-with-raise.py)
- Base case `n == 0 or n == 1`. For invalid input, `raise ValueError(...)` instead of printing and returning: a bare `return` gives back `None`, which then gets printed as well.
- Uncaught, `raise` crashes with a traceback; catch it with `try / except ValueError` when you want a clean message.
- Python's default recursion limit is about 1000 frames, so very deep recursion needs a loop or `sys.setrecursionlimit`.

**Fibonacci** — [fibonacci-recursive.py](../solutions/recursion/fibonacci-recursive.py)
- This version uses `fibo(0) = fibo(1) = 1`, so `fibo(5) = 8`. The textbook sequence starts `0, 1, 1, 2, 3, 5`, giving `fib(5) = 5`. Check which indexing the problem uses.
- Plain recursion is O(2ⁿ) because the same subproblems are recomputed. Add a cache (`functools.lru_cache`) to make it O(n).

**Reverse an array** — [reverse-array.py](../solutions/recursion/reverse-array.py)
- Two indices, `front` and `rear`. Base case `front >= rear`; otherwise swap and recurse on `front+1, rear-1`. Works in place, so the recursive call's return value isn't needed.

**Palindrome check** — [palindrome-check-recursive.py](../solutions/recursion/palindrome-check-recursive.py)
- Compare the two ends; mismatch means not a palindrome; otherwise recurse inward. Base case `front >= end` covers both the empty string and a single character (tested: `""`, `"a"`, `"aba"`, `"abba"`, `"abca"`).

**Bubble and insertion sort, recursive** — see [arrays-hashing.md](arrays-hashing.md)
- The recursion replaces the outer loop; the base case is "no swaps this pass" for bubble and `x == len(arr)` for insertion.

## Number theory

**Count digits** — [count-digits.py](../solutions/math-geometry/count-digits.py)
- `len(str(abs(n)))`, or divide by 10 until zero. Zero is a special case: it has one digit, but the divide loop would give zero.

**Palindrome number** — [palindrome-number.py](../solutions/math-geometry/palindrome-number.py)
- Reverse the digits with `% 10` and `// 10`, compare with the original. Negative numbers are never palindromes, and the loop `while x > 0` handles them naturally.

**GCD** — [gcd-via-common-divisors.py](../solutions/math-geometry/gcd-via-common-divisors.py)
- The repo version lists both numbers' divisors and takes the largest common one. The efficient method is Euclid: `gcd(a, b) = gcd(b, a % b)` until `b == 0`, O(log n).

**Armstrong number** — [armstrong-number.py](../solutions/math-geometry/armstrong-number.py)
- Sum of each digit raised to the number of digits equals the number itself. Compute the digit count once, outside the loop. Checked for 0..1999.

**All divisors** — [find-divisors.py](../solutions/math-geometry/find-divisors.py)
- Loop `i` while `i * i <= n`; every `i` that divides `n` gives two divisors, `i` and `n // i`. Skip the second when they are equal (perfect squares). O(√n).
- The output is interleaved (`[1, 12, 2, 6, 3, 4]` for 12), not sorted. Sort it if the problem asks for order.

**Prime check** — [prime-check.py](../solutions/math-geometry/prime-check.py)
- Try divisors `2 .. √n`; any hit means composite.
- **Re-test:** add `if n < 2: not prime` first. Right now `1`, `0` and negative numbers print "Prime".

## Fast power

**Pow(x, n)** — [pow-x-n.py](../solutions/recursion/pow-x-n.py)
- Binary exponentiation: compute `half = x^(n//2)` once, then return `half * half` (n even) or `half * half * x` (n odd). That is O(log n) multiplications instead of n, which is what makes `n = 2^31 - 1` possible.
- The key is calling the recursion **once** and squaring the result. Writing `checker(x, n//2) * checker(x, n//2)` looks the same but makes two calls at every level, which is back to O(n).
- Negative n: compute the positive power first and divide once at the end, `x^-n = 1 / x^n`. The first version flipped `x = 1/x` at the start instead; the rounding error in `1/x` then got raised to the power n and LeetCode failed it on the last digit. The fixed version (2026-10-01) passes.
- Recursion depth is about log2(n), so at most ~32 calls: no recursion-limit problem.
- **Precision trap (fails on LeetCode):** when `x` is very close to 1 and `|n|` is huge (e.g. `x = 0.9999999953`, `n = -1951257921`, answer about 8928), each squaring adds a tiny rounding error and the ~31 squarings multiply it up, so the answer is off in the 3rd decimal (8928.11033 instead of 8928.10877). My first check skipped these inputs, so it wrongly reported all correct. Flipping `x = 1/x` at the start makes it worse, because the rounding error in `1/x` gets raised to the power n too; computing `x^|n|` and taking `1/result` at the end (the current version) halves the worst error and passes LeetCode, though tiny errors remain on extreme inputs. Python's `x ** n` is accurate to the last digit on the same inputs.
- `n = 0` returns the integer `1` rather than `1.0`. LeetCode accepts it, but `1.0` matches the float return type.
- In Java or C++, `abs(-2^31)` overflows a 32-bit int. Convert `n` to `long` first. Python has no such problem.

**Count good numbers** — [count-good-numbers.py](../solutions/recursion/count-good-numbers.py)
- Even positions (0, 2, 4, ...) can hold an even digit: 5 choices (0, 2, 4, 6, 8). Odd positions can hold a prime digit: 4 choices (2, 3, 5, 7). The positions are independent, so the answer is `5^even * 4^odd` with `even = (n + 1) // 2` and `odd = n // 2`.
- `n` goes up to 10^15, so the powers must be computed with modular fast power. Python's built-in `pow(base, exp, mod)` does exactly the binary exponentiation from Pow(x, n), keeping every step below `mod`. Writing `5**even % mod` would try to build a number with ~700 trillion digits.
- Take `% mod` after multiplying the two powers too; each is below `mod`, but their product is not.
- Checked against brute force (every digit string) for n = 1 to 7 and the known answers for n = 1, 4, 50: all correct. n = 10^15 runs instantly.
- In an interview you may be asked to write the modular power yourself: same as Pow(x, n), with `% mod` after every multiplication.

## Backtracking

**Generate parentheses** — [generate-parentheses.py](../solutions/recursion/generate-parentheses.py)
- Build the string one character at a time and only make moves that can still lead to a valid answer: add `(` while `open < n`, add `)` while `close < open`. Because invalid prefixes are never built, every finished string is valid and nothing has to be checked or filtered at the end.
- Base case: `open == n and close == n` means the string has length `2n`, so save it. Here the check sits after the two recursive calls; it still works because at that point neither `if` fires, but putting the base case first is the usual habit and reads more clearly.
- Passing `curr + '('` creates a new string for each call, so there is nothing to undo. With a list you would `append`, recurse, then `pop` (the explicit "backtrack" step).
- Count of answers is the Catalan number (1, 2, 5, 14, 42, ... 16,796 for n = 10). Checked against brute force (every string of `(` and `)` filtered for validity) for n = 0 to 9: exact match, no duplicates.
- `open` shadows Python's built-in `open()` inside the function; `opened` or `left` avoids that.

**Reverse a stack** — [reverse-a-stack.py](../solutions/recursion/reverse-a-stack.py)
- Pop everything into a second list: the first item popped (the top) becomes the first item of the new list, so the order is reversed. Then `st.extend(sy)` puts it back, so the original stack is reversed in place and the same list is returned. O(n) time, O(n) extra space.
- Checked on 3,000 random lists, including empty: the stack and the returned list are both the reversed input.
- This is the simple, practical answer. The problem sits in the Recursion module because the interview version bans extra containers and loops: reverse using only recursion, with two helpers. `reverse(st)`: pop the top, reverse the rest, then call `insert_at_bottom(st, top)`. `insert_at_bottom(st, x)`: if empty push `x`, otherwise pop, recurse, push back. That is O(n²) time and O(n) recursion depth, no extra list. It is worth writing once, because "insert at the bottom of a stack" comes up on its own (sort a stack uses the same trick).
- Note: a Python list is only a stack if you use `append` and `pop()` at the end. `pop(0)` is O(n).

**Check if a subsequence with sum K exists** — [subsequence-sum-k-exists.py](../solutions/recursion/subsequence-sum-k-exists.py)
- Pick / not-pick again, carrying the running sum. Return `True` as soon as `sum == k`, and `False` when the index runs out. The `or` between the two calls stops at the first success, so no other branch is explored after an answer is found.
- The first version (no pruning) hit TLE on the judge. Adding `or sum>k` to the failure test made it pass: with non-negative numbers, once the sum goes past `k` it can never come back, so the whole branch is cut. The `sum==k` check must stay before the length check.
- Checked against a brute force on 20,000 inputs: no mismatches. The empty subsequence counts, so `k = 0` is `True`.
- Still 2^n in the worst case: when the numbers are small and `k` is huge the sum never passes `k`, so nothing is pruned (26 ones with k = 10^6 takes 20s here; every +2 elements is about 4x slower). It passes because the judge's tests have a `k` the pruning can cut, or few elements. For a guaranteed fast answer, remember each `(index, sum)` already tried (memoization) or use a reachable-sums array (subset-sum DP), both O(n·k).
- The pruning is only valid for non-negative numbers; with negatives the sum can drop back to `k`.
- `sum` shadows the built-in `sum`.

**Count subsequences with sum K** — [count-subsequences-sum-k.py](../solutions/recursion/count-subsequences-sum-k.py)
- Same pick / not-pick recursion as "does a subsequence exist", but each call returns a number and the two branches are **added** (`+` instead of `or`). A base case that matches returns 1, a dead end returns 0. All branches must run, so there is no early exit.
- Why `count += 1` did not work: a number passed into a function is copied, so the change stays inside that call. Either return the counts (best) or keep the total in a list/dict that every call shares.
- The first pushed version (2026-10-04) had two typos and did not run: a 3-space indent on the final `return` (`IndentationError`) and `arr` instead of `nums` in `Solution` (`NameError`). It was replaced the same day with the corrected file.
- The corrected file decides only at the end of the array (`if i == len(arr): return 1 if sum == k else 0`) and prunes with `if sum > k: return 0`. Checked against a brute force on 20,000 inputs including zeros: 0 wrong. The earlier `if sum == k: return 1` version was fine for positive numbers but undercounted with 0s (`[3, 0]`, `k = 3` gave 1, answer is 2), because it stopped before considering the 0.
- Counting cannot stop early, so it is slower than the exists version on big inputs. Store each `(i, sum)` answer in a dict (memoization) to make it O(n·k).

**Power set (all subsequences of a string)** — [power-set.py](../solutions/recursion/power-set.py)
- Pick / not-pick: at each index make two calls, one that skips `s[index]` and one that adds it. When `index == len(s)` the current string is one finished subsequence. That gives 2^n results in O(n · 2^n) time.
- This pick / not-pick tree is the template for the rest of the module (subsequence sum K, Combination Sum, Subsets I and II).
- Checked against `itertools.combinations` on 3,000 strings: the same list in the same sorted order.
- The empty string `""` is included (it is the "skip everything" branch). Some versions of the problem, including GfG's "non-empty subsequences" wording, expect it left out. If a judge rejects it, drop `""` before returning.
- Repeated letters give repeated subsequences (`"aa"` gives `"a"` twice). That is correct when the problem counts positions; for unique subsets you need the Subsets II technique (sort, then skip equal neighbours at the same level).
- The `return result` in the base case is never used by the caller; a plain `return` does the same.

**Binary strings with no two adjacent zeros** — [binary-strings-no-adjacent-zeros.py](../solutions/recursion/binary-strings-no-adjacent-zeros.py)
- Build the string one character at a time. A `1` can always be added. A `0` can be added only when the string is empty or ends in `1`. Because invalid moves are never made, every string of length `n` that is reached is valid and goes straight into `result`. Same idea as Generate Parentheses: only make moves that can still lead to a valid answer.
- Number of answers is Fibonacci-like: 2, 3, 5, 8, ... (`n = 3` gives 5: 111, 110, 101, 011, 010). Checked against a brute force (all 2^n strings, drop any containing `00`) for n = 1 to 14: exact match, no duplicates.
- This is LeetCode 3211, "no two adjacent **zeros**". The sheet's title says "without consecutive **1s**", which is the same problem with 0 and 1 swapped; to switch, add `0` always and `1` only after a `0` (or at the start).
- The order of the output is not sorted (`1` is tried before `0`). LeetCode accepts any order; if a judge wants sorted order, try `0` first.
- Cleaned the whitespace and used 4-space indents before pushing (the logic is unchanged).

**Combination Sum** — [combination-sum.py](../solutions/recursion/combination-sum.py)
- Pick / not-pick with one difference: after **picking** `candidates[i]` you stay on the same index (`checker(i, ...)`) because a number may be used again and again; after **not picking** you move on (`checker(i+1, ...)`). Moving on is what stops the same combination from being built in a different order, so there are no duplicates.
- Base cases: `sum == target` saves a copy of the path, `i == len(candidates)` or `sum > target` is a dead end. The `sum > target` cut is only valid because all numbers are positive.
- `curr + [x]` builds a new list each call, so saved paths never change later. With one shared list you must save `curr[:]` and `pop()` after the recursive call (the usual backtracking form).
- Checked against a brute force on 5,000 random inputs (distinct candidates 2..11, target up to 25): same set of combinations, no duplicates. `[2,3,6,7]`, target 7 gives `[[2,2,3],[7]]`.
- Relies on the problem's rule that candidates are at least 1: a 0 would make `checker(i, ...)` repeat forever.
- Cleaned the whitespace before pushing (the logic is unchanged).

## Pascal's triangle

**Element at row N, column c** — [row building](../solutions/math-geometry/pascals-triangle-element.py), [direct formula](../solutions/math-geometry/pascals-triangle-element-formula.py)
- Element = C(N-1, c-1). Row building constructs each row from the previous one: O(N²).
- The direct formula multiplies and divides as it goes, O(c): start `prev = 1` and for `i = 1 .. c-1` do `prev = prev * (N - i) / i`. For N=5, c=3 that gives 4 then 6.
- **Re-test:** use integer division `//`. The intermediate value is always an exact integer, but the `/` version goes through floats and `int()` truncates: row 12, column 6 returns 461 (correct: 462), and large rows are off by one or more.
