class Solution:
    # TC --> O(1), SC --> O(1)
    def findClosest(self, x: int, y: int, z: int) -> int:
        xz = abs(x-z)
        yz = abs(y-z)
        if xz < yz:
            return 1
        if xz > yz:
            return 2
        else:
            return 0