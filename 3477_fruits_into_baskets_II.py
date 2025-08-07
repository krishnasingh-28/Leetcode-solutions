class Solution:
    # TC --> O(N^2), SC --> O(1)
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        n = len(baskets)
        for fruit in fruits:
            flag = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    flag = 0
                    break
            count += flag
        return count
