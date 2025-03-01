class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # TC --> O(N), SC --> O(1)
        indexes = [] # i,j
        for i in range(len(s1)): # going through the string
            if s1[i] != s2[i]: # comparing both the string in the linear manner
                indexes.append(i)# if there is a mismatch append it to array
            if len(indexes) > 2:# if more than 2 elements for swap return false
                return False
        if len(indexes) == 2:# if exact 2 elements in array compare with both str 
            i, j = indexes # assign the i and j pointers in the array 
            # do match the following with both the strings
            if s1[i] == s2[j] and s1[j] == s2[i]:
                return True
            else:
                return False
        if len(indexes) == 0: # edge case if both the str is already same
            return True
        return False
