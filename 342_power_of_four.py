class Solution:
    # TC --> O(1), SC --> O(1)
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(16):
            power_of_four = 4**i
            if power_of_four == n:
                return True
            if power_of_four > n:
                return False
        return False