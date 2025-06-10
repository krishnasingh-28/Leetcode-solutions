class Solution:
    # TC --> O(N), SC --> O(K)
    def maxDifference(self, s: str) -> int:
        char_count = Counter(s)
        odd_count = []
        even_count = []
        for freq in char_count.values():
            if freq % 2 == 1:
                odd_count.append(freq)
            else:
                even_count.append(freq)
        max_odd = max(odd_count)
        min_even = min(even_count)
        return max_odd - min_even