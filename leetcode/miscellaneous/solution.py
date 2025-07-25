class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l[-1])


obj = Solution()
print(obj.lengthOfLastWord("   fly me   to   the moon  "))