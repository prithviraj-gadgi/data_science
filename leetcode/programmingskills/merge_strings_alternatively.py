class Solution:
    def merge_strings_alternatively(self, a: str, b: str) -> str:
        result = []
        max_length = max(len(a), len(b))

        for i in range(max_length):
            if i < len(a):
                result.append(a[i])
            if i < len(b):
                result.append(b[i])

        return "".join(result)


solution = Solution()
print(solution.merge_strings_alternatively("abc", "def"))
