class Solution:
    # TC --> O(N), SC --> O(1)
    def secondHighest(self, s: str) -> int:
        digits = set()
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
        if len(digits) < 2:
            return -1
        digits = sorted(digits, reverse=True)
        return digits[1]
