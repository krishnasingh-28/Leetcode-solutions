class Solution:
    # TC --> O(N), SC -->O(N)
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)