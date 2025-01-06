class Solution:
    # EXAMPLE FOR VARIABLE SIZED SLIDING WINDOW
    # TC --> O(N), SC --> O(N) [since the set requires n spaces]
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0  # starting point of the window
        longest = 0 # longest length
        sett = set() # thus to avoid storing duplicate characters
        n = len(s) 
        for r in range(n): # r is the ending point of the window to catch the substring
            while s[r] in sett: # invalid case (i.e if duplicate chars are already present)
                sett.remove(s[l]) # remove the already existing char of s[l] from the sett
                l += 1 # increment of the starting point of the window
            w = (r-l) + 1  # formula for calculating the length of the substring window
            longest = max(longest, w)
            sett.add(s[r]) # add the distinct char which is not present in sett to make valid
        return longest 