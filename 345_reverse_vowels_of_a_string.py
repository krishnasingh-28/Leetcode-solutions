class Solution:
    # TC --> O(N), SC --> O(1)
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        s = list(s)
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] not in vowels and s[r] not in vowels:
                l += 1
                r -= 1
            elif s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return "".join(s)
