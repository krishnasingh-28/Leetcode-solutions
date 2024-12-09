class Solution:
    # TC --> O(N log N), SC --> O(N)
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        result = ""
        for key in sorted(hashmap, key = hashmap.get, reverse = True ):
            result += key * hashmap[key]
        return result