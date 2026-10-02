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

## Backtracking

**Generate parentheses** — [generate-parentheses.py](../solutions/recursion/generate-parentheses.py)
- Build the string one character at a time and only make moves that can still lead to a valid answer: add `(` while `open < n`, add `)` while `close < open`. Because invalid prefixes are never built, every finished string is valid and nothing has to be checked or filtered at the end.
- Base case: `open == n and close == n` means the string has length `2n`, so save it. Here the check sits after the two recursive calls; it still works because at that point neither `if` fires, but putting the base case first is the usual habit and reads more clearly.
- Passing `curr + '('` creates a new string for each call, so there is nothing to undo. With a list you would `append`, recurse, then `pop` (the explicit "backtrack" step).
- Count of answers is the Catalan number (1, 2, 5, 14, 42, ... 16,796 for n = 10). Checked against brute force (every string of `(` and `)` filtered for validity) for n = 0 to 9: exact match, no duplicates.
- `open` shadows Python's built-in `open()` inside the function; `opened` or `left` avoids that.

**Power set (all subsequences of a string)** — [power-set.py](../solutions/recursion/power-set.py)
- Pick / not-pick: at each index make two calls, one that skips `s[index]` and one that adds it. When `index == len(s)` the current string is one finished subsequence. That gives 2^n results in O(n · 2^n) time.
- This pick / not-pick tree is the template for the rest of the module (subsequence sum K, Combination Sum, Subsets I and II).
- Checked against `itertools.combinations` on 3,000 strings: the same list in the same sorted order.
- The empty string `""` is included (it is the "skip everything" branch). Some versions of the problem, including GfG's "non-empty subsequences" wording, expect it left out. If a judge rejects it, drop `""` before returning.
- Repeated letters give repeated subsequences (`"aa"` gives `"a"` twice). That is correct when the problem counts positions; for unique subsets you need the Subsets II technique (sort, then skip equal neighbours at the same level).
- The `return result` in the base case is never used by the caller; a plain `return` does the same.

## Pascal's triangle

**Element at row N, column c** — [row building](../solutions/math-geometry/pascals-triangle-element.py), [direct formula](../solutions/math-geometry/pascals-triangle-element-formula.py)
- Element = C(N-1, c-1). Row building constructs each row from the previous one: O(N²).
- The direct formula multiplies and divides as it goes, O(c): start `prev = 1` and for `i = 1 .. c-1` do `prev = prev * (N - i) / i`. For N=5, c=3 that gives 4 then 6.
- **Re-test:** use integer division `//`. The intermediate value is always an exact integer, but the `/` version goes through floats and `int()` truncates: row 12, column 6 returns 461 (correct: 462), and large rows are off by one or more.
