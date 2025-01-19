class Solution:
    def index_of_first_occurrence(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


solution = Solution()
print(solution.index_of_first_occurrence("sadabcsad", "sad"))
