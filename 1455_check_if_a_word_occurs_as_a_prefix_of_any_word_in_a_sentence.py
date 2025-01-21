class Solution:
    # TC --> O(N), SC --> O(1)    
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words, 1):
            if word[: len(searchWord)] == searchWord:
                return i
        return -1