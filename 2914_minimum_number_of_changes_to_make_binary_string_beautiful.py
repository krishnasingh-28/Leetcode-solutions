class Solution:
    #TC --> O(N), SC-->O(1)
    def minChanges(self, s: str) -> int:
        count = 0 # to track the count 
        for i in range(0,len(s),2): # loop to run the entire string by 2 steps
            if s[i] != s[i+1]:#checking the neighbouring element with current element
                count += 1 # increasing count
        return count