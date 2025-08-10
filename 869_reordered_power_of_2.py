class Solution:
    # TC --> O(N log N), SC --> O(N)
    def reorderedPowerOf2(self, n: int) -> bool:
        s = sorted(str(n))
        for i in range(30):
            power2 = 1 << i  # this is a fast way to do 2**i
            p_s = sorted(str(power2))  # creating a signature for the power of 2
            if s == p_s:  # if signature matches we found it
                return True
        return False
