from collections import Counter


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


solution = Solution()
print(solution.is_anagram("aba", "aab"))
