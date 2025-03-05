class Solution:
    # TC --> O(log N), SC --> O(1) using binary search
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n # Search space from 1 to n
        total_sum = n * (n + 1) // 2 # Sum of first n numbers
        while left < right:
            mid = (left + right) // 2# Find the middle element
            # mid*mid - total_sum is derived from the equation we need to satisfy
            if mid * mid - total_sum < 0:
                left = mid + 1  # Move right
            else:
                right = mid  # Move left
        # Final check if the pivot integer satisfies the condition
        if left * left - total_sum == 0:
            return left
        else:
            return -1  # If no pivot integer is found
