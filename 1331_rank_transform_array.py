class Solution:
    # TC -->O(N log N), SC --> O(N)
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_set = sorted(set(arr))#  Sorting the array in ascending order & removing the duplicates
        rank_map = {} # empty dictionary to store (key--> arr : value--> rank) pairs 
        for i, a in enumerate(sorted_set): # i is the index and a is an element to iterate over the sorted set
            rank_map[a] = i + 1 # starting the rank with 1
        rank = [] # empty list to reserve the ranks
        for a in arr:  # iterating over the original arr
            rank.append(rank_map[a]) # fetching the rank and appending it according to the original array
        return rank 