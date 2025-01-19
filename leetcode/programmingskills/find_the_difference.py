class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        for i in t:
            if t.count(i) != s.count(i):
                return i


solution = Solution()
print(solution.find_the_difference("abc", "abcc"))
