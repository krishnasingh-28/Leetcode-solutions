class Solution:
    # TC --> O(N log log N), SC --> O(N)
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                # Mark multiples of i starting from i*i as not prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return count
