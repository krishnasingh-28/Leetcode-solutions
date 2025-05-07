class Solution:
    # Converting to String
    # TC --> O(N log M), SC --> O(log M)
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            length = len(str(n))
            if length % 2 == 0:
                count += 1
        return count
    
    # Manual Counting
    # TC --> O(N log M), SC --> O(1)
    def count_digits(self, n):
        digits = 0
        while n > 0:
            digits += 1
            n = n // 10
        return digits

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if self.count_digits(num) % 2 == 0:
                count += 1
        return count
