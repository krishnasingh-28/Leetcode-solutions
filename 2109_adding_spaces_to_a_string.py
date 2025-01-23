class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # TC --> O(N), SC --> O(N)
        space_index = 0 
        result = []
        for string_index in range(len(s)):
            if space_index < len(spaces) and string_index == spaces[space_index]:
                result.append(" ")
                space_index += 1
            result.append(s[string_index])
        final_string = "".join(result)
        return final_string