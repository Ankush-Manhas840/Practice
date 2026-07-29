"""
Concentric Number Square
------------------------
Topic      : pattern-printing
Difficulty : Hard

Problem
    Given n, print a (2n-1) x (2n-1) square where each cell holds a number
    determined by how far it sits from the nearest edge. The outermost ring
    is n, the next ring in is n-1, and so on down to 1 at the centre.

Example (n = 6)
    66666666666
    65555555556
    65444444456
    65433333456
    65432223456
    65432123456
    65432223456
    65433333456
    65444444456
    65555555556
    66666666666

Approach
    For every cell (x, y) compute its distance to each of the four edges:
        top    = x - 1
        bottom = size - x
        left   = y - 1
        right  = size - y
    The smallest of those four is the ring index (0 for the outer ring).
    Subtracting it from n gives the value to print.

Complexity
    Time  : O(n^2) -- every cell is visited once
    Space : O(1)   -- printed directly, nothing stored
"""


def concentric_number_square(n):
    size = n * 2 - 1

    for x in range(1, size + 1):
        for y in range(1, size + 1):
            top = x - 1
            bottom = size - x
            left = y - 1
            right = size - y
            print(n - min(top, bottom, left, right), end="")
        print()


if __name__ == "__main__":
    concentric_number_square(6)
