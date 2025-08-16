class Solution:
    def maximum69Number(self, num: int) -> int:
        # TC --> O(N), SC --> O(N)
        num_str = str(num)
        # replacing string of '6' with '9' on its 1st occurrence
        new_num_str = num_str.replace("6", "9", 1)
        return int(new_num_str)
