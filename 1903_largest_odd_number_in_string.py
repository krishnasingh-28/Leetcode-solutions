class Solution:
    # TC --> O(N), SC --> O(1)
    def largestOddNumber(self, num: str) -> str:
        j = -1
        i = 0
        for i in range(len(num)-1, -1, -1):
            if (int(num[i]) % 2 == 1):
                j = i
                break
        # Skipping the Leading zeros
        i = 0 
        while i <= j and num[i] == '0':
            i += 1
        return num[i:j+1]