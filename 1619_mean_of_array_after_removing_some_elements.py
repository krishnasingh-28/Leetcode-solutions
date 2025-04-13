class Solution:
    # TC --> O(N log N), SC --> O(N) 
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        length = len(arr)
        remove = int(length * 0.05)
        remain = arr[remove : length - remove]
        mean = sum(remain) / len(remain)
        return mean
