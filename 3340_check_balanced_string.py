class Solution:
    # TC --> O(N), SC --> O(1)
    def isBalanced(self, num: str) -> bool:
        odd_sum = 0
        even_sum = 0
        for i in range(1,len(num),2):
            odd_sum += int(num[i])
        for j in range(0,len(num),2):
            even_sum += int(num[j])
        if odd_sum == even_sum:
            return True
        
        return False