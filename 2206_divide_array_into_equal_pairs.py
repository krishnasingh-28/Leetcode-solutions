class Solution:
    # Approach 1
    # TC --> O(N log N), SC --> O(1) 
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums),2):
            if nums[i] != nums[i-1]:
                return False
        return True
    
    # Approach 2
    # TC --> O(N), SC --> O(N) 
    def divideArray(self, nums: List[int]) -> bool:
        odd_set = set()
        for n in nums:
            if n not in odd_set:
                odd_set.add(n)
            else:
                odd_set.remove(n)
        if len(odd_set) != 0:
            return False
        return True
    
    # Approach 3
    # TC --> O(N), SC --> O(N) 
    def divideArray(self, nums: List[int]) -> bool:
        count = {} # create a hashmap
        for n in nums: # access the key from nums
            if n not in count: # if key not in dict
                count[n] = 0 # make frequency count as 0
            count[n] += 1# else increase the frequency count
        
        # accessing the key-value pair
        for n, cnt in count.items(): 
            if cnt % 2 != 0: # frequency must be even 
                return False
        return True