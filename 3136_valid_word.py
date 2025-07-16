class Solution:
    # TC --> O(N), SC --> O(1)
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowel = False
        consonant = False
        for i in word:
            if i.isalpha():
                if i.lower() in "aeiouAEIOU":
                    vowel = True
                else:
                    consonant = True
            elif not i.isdigit():
                return False
        return vowel and consonant
