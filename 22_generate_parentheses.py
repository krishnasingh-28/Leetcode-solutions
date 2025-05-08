class Solution:
    # Using Recursion  TC --> O(4^n / sqrt(n), SC --> O(4^n / sqrt(n))
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(0, 0, n, "", ans)
        return ans

    def generate(
        self, open_count: int, close_count: int, n: int, current: str, ans: list
    ):
        if open_count == close_count == n:
            ans.append(current)
            return
        if open_count < n:
            self.generate(open_count + 1, close_count, n, current + "(", ans)
        if close_count < open_count:
            self.generate(open_count, close_count + 1, n, current + ")", ans)
