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

## Pascal's triangle

**Element at row N, column c** — [row building](../solutions/math-geometry/pascals-triangle-element.py), [direct formula](../solutions/math-geometry/pascals-triangle-element-formula.py)
- Element = C(N-1, c-1). Row building constructs each row from the previous one: O(N²).
- The direct formula multiplies and divides as it goes, O(c): start `prev = 1` and for `i = 1 .. c-1` do `prev = prev * (N - i) / i`. For N=5, c=3 that gives 4 then 6.
- **Re-test:** use integer division `//`. The intermediate value is always an exact integer, but the `/` version goes through floats and `int()` truncates: row 12, column 6 returns 461 (correct: 462), and large rows are off by one or more.
