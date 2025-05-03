class Solution:
    # TC --> O(N log N), SC --> O(N)
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        hashmap = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                hashmap[s] = "Gold Medal"
            elif i == 1:
                hashmap[s] = "Silver Medal"
            elif i == 2:
                hashmap[s] = "Bronze Medal"
            else:
                hashmap[s] = str(i + 1)
        return [hashmap[s] for s in score]
