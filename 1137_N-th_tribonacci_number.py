class Solution:
    # TC --> O(N), SC --> O(1)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            d = a + b + c
            a = b
            b = c
            c = d
        return c