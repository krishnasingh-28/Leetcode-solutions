class Solution:
    # Approach 1 
    # TC --> O(N), SC --> O(1)
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False

    # Approach 2 
    # TC --> O(N), SC --> O(1)
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0
        for n in arr:
            if n % 2 == 1:
                consecutive_odds += 1
            else:
                consecutive_odds = 0
            if consecutive_odds == 3:
                return True
        return False
    
    # Approach 3
    # TC --> O(N), SC --> O(1)
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            product = arr[i] * arr[i + 1] * arr[i + 2]
            if product % 2 == 1:
                return True
        return False