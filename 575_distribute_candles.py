class Solution:
    # TC --> O(K), SC --> O(U)
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        Len = len(set(candyType))
        return min(n, Len)