class Solution:
    # TC --> O(N.M), SC --> O(min(N,M)) extra space is by intermediate array which is used for reversing
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        N, M = len(mat), len(mat[0])# N:rows, M:cols
        res, intermediate = [], []
        for diagonal in range(N + M - 1):
            intermediate.clear()
            if diagonal < M:
                r = 0
                c = diagonal
            else:
                r = diagonal - M + 1
                c = M - 1
            while r < N and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            # Reverse even numbered diagonals. The
            # logic says we have to reverse odd
            # numbered articles but here, the numbering
            # is starting from 0
            if diagonal % 2 == 0:
                res.extend(intermediate[::-1])
            else:
                res.extend(intermediate)
        return res
