class Solution:
    # TC --> O(N), SC --> O(k)
    def kthFactor(self, n: int, k: int) -> int:
        factor_count = 0
        for i in range(1, n+1):
            if n % i == 0:
                factor_count += 1
                if factor_count == k:
                    return i
        return -1