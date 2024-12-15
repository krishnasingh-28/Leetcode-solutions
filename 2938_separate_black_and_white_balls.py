class Solution:
    def minimumSteps(self, s: str) -> int:
        # TC --> O(N), SC --> O(1)
        total_swaps = 0 # to keep track of the total number of swaps required.
        black_ball_count = 0 # to count the number of black balls encountered.
        for char in s:
            if char == '0':
                total_swaps += black_ball_count
            else:           #If it is not 0 (meaning it's a black ball)
                black_ball_count += 1
        return total_swaps