class Solution:
    # TC --> O(N),  SC --> O(1)
    def minSwaps(self, s: str) -> int:
        count = 0 
        for ch in s:
            if ch == '[':
                count += 1
            elif count > 0:
                count -= 1
        return (count + 1) // 2