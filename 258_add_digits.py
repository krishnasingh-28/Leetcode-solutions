class Solution:
    # Brute Force 
    # TC --> O(log(num)), SC --> O(1)
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            num = s
        return num
    
    # Optimal approach
    # TC --> O(1), SC --> O(1)
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
