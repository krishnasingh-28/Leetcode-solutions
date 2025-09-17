class Solution:
    # TC --> O(N), SC --> O(N) iteration using two pass
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans
