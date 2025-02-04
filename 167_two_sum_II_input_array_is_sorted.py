class Solution:
    # TC -->O(N^2), using brute force approach, SC -->O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        return []
    
    # TC -->O(N log N), using optimal approach(binary search), SC -->O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            temp = target - numbers[i]
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == temp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < temp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []