class Solution:
    # TC --> O(N), SC --> O(N)
    def isValid(self, s: str) -> bool:
        st = []
        # Mapping of closing to opening brackets
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                st.append(char)
            elif char in mapping:  # If it's a closing bracket
                if not st or st[-1] != mapping[char]:  # Check stack and match
                    return False
                st.pop()  # Remove the matching opening bracket
            else:
                return False  # Invalid character

        # Stack should be empty if all brackets are valid
        return not st
