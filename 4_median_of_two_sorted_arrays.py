class Solution:
    # TC --> O((m+n)*log(m+n)), SC --> O(m+n)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            return float(arr[n//2])
        else:
            return (arr[n//2-1] + arr[n//2])/2.0
            