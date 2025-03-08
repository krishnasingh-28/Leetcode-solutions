class Solution:
    # TC --> O(N^2), SC --> O(N)
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part,"",1) 
        return s