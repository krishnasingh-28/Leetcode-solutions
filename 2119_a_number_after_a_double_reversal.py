# TC --> O(2N), SC --> O(1)
def reverse(n):
    rev = 0
    while n != 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n //= 10
    return rev
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        rev1 = reverse(num)
        rev2 = reverse(rev1)
        return num == rev2
    
    
    
    
    # TC --> O(1), SC-->O(1)
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        else:
            return True