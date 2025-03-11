class Solution:
    # TC --> O(N), SC --> O(1)
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26