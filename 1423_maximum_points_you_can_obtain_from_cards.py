class Solution:
    # Constant Window 
    # TC --> O(2*K) where K is the size of the window, SC --> O(1)
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum, maxSum = 0, 0, 0
        # Calculate the initial sum of the first k cards
        for i in range(k): 
            lsum = lsum + cardPoints[i]
            maxSum = lsum
        # Initialize rightIndex to iterate array from last
        rightIndex = len(cardPoints) - 1
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i] # Remove the Points of the ith card from left sum
            rsum += cardPoints[rightIndex]#Add the Points from the right to the rsum
            rightIndex -= 1  # Move to the next card from the right
            maxSum = max(maxSum, lsum + rsum)#Update maxSum with the maximum sum 
        return maxSum