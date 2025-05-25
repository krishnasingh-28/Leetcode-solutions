from math import isqrt
class Solution:
    # TC --> O(N^2), SC --> O(P)
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(self, n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, isqrt(n) + 1, 2):
                if n % i == 0:
                    return False
            return True
        prime_set = set()
        # Generate substrings
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]

                # Skip substrings with leading zeros (but allow "0")
                if substring.startswith("0") and len(substring) > 1:
                    continue

                num = int(substring)
                if is_prime(self, num):
                    prime_set.add(num)

        largest_primes = sorted(prime_set, reverse=True)[:3]
        return sum(largest_primes)
