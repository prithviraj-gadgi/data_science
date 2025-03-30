from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        print(anagram_map)

        for value in anagram_map.values():
            result.append(value)

        return result

solution = Solution()
strs_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(solution.group_anagrams(strs_list))