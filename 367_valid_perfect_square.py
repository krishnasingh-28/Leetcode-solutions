class Solution:
    # TC --> O(log N), SC --> O(1)
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l = 1
        r = num // 2
        while l <= r:
            m = l + (r - l) // 2
            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            else:
                r = m - 1
        return False
