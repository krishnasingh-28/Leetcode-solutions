class Solution:
    # TC --> O(1), SC --> O(1)
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.capitalize() or word == word.lower():
            return True
        else:
            return False