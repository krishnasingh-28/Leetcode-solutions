class Solution:
    # Brute Force approach
    # TC --> O(N^3 x log(no of unique triplets)), SC-->O(2x no of unique triplets)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_set = set()
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i]+ nums[j]+ nums[k]) == 0:
                        temp = [nums[i],nums[j], nums[k]]
                        temp.sort()
                        triplet_set.add(tuple(temp))
        ans = [list(triplet) for triplet in triplet_set]
        return ans
    
    # Better approach
    # TC --> O(N^2 x log(no of unique triplets)), SC-->O(2x no of unique triplets) + O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplet_set = set()
        n = len(nums)
        for i in range(n):
            hashset = set()
            for j in range(i+1, n):
                third = -(nums[i] + nums[j])
                if third in hashset:
                    temp = [nums[i],nums[j], third]
                    temp.sort()
                    triplet_set.add(tuple(temp))
                hashset.add(nums[j])
        ans = [list(triplet) for triplet in triplet_set]
        return ans
    
    # Optimal approach
    # TC --> O((N log N) + O(N^2)), SC-->O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum_val = nums[i] + nums[j] + nums[k]
                if sum_val < 0:
                    j += 1
                elif sum_val > 0:
                    k -= 1
                else:
                    temp =[nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return ans