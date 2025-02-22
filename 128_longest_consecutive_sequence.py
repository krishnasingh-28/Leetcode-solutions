class Solution:
    # Optimal Approach using unordered set
    # TC --> O(2N), SC --> O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        if n == 0:
            return 0
        longest = 1
        st = set()
        for i in range(n):
            st.add(nums[i])
        for it in st:
            if it - 1 not in st:
                cnt = 1
                x = it
                while x + 1 in st:
                    x = x + 1
                    cnt += 1
            longest = max(cnt, longest)
        return longest
