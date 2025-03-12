class Solution:
    # Approach 1
    # TC --> O(N), SC --> O(N)
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        return " ".join(words[0:k])
    
    # Approach 2
    # TC --> O(N), SC --> O(N)
    def truncateSentence(self, s: str, k: int) -> str:
        cnt = 0
        for i,c in enumerate(s):
            if c == " ":
                cnt += 1
                if cnt == k:
                    return s[:i]
        return s