class Solution:
    # TC --> O(NLogN+MLogM), SC --> O(1)
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        only_in_nums1 = sorted(set1 - set2)
        only_in_nums2 = sorted(set2 - set1)

        return [only_in_nums1, only_in_nums2]