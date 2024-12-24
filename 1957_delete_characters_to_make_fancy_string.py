class Solution:
    # TC --> O(N), SC --> O(1)
    def makeFancyString(self, s: str) -> str:
        count = 1# it counts the consecutive occurrences of prev
        prev = s[0] # 1st element
        ans = s[0] # new string starting from the first letter
        for i in range(1, len(s)): # looping from the second element
            if s[i] == prev: 
                count += 1 # track of previous count
            else:
                prev = s[i] # incrementing the prev to the next char
                count = 1 # reset the count to 1 hence the new char is found
            if count < 3:
                ans += s[i] # append the s[i] to ans
        return ans