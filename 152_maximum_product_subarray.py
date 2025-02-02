class Solution:
    # TC-->O(N), SC-->O(1)
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                # Swap max_product and min_product when encountering a negative number
                max_product, min_product = min_product, max_product
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            result = max(result, max_product)
        return result