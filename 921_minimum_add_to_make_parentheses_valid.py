class Solution:
    # TC --> O(N), SC --> O(1)
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0 
        minaddrequired = 0
        for char in s:
            if char == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    minaddrequired += 1
        return open_brackets + minaddrequired
        