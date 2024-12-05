class Solution:
    # TC --> O(N*log N + M), SC --> O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        n = len(strs)
        strs.sort()
        first, last = strs[0], strs[n-1]
        ans = []
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ''.join(ans)
            ans.append(first[i])
        return ''.join(ans)