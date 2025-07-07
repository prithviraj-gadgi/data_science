# def countValidWords(s):
#     vowels = set('aeiouAEIOU')
#     count = 0
#
#     for word in s.split():
#         # 1) must be at least 3 chars
#         if len(word) < 3:
#             continue
#
#         # 2) only alphanumeric
#         if not word.isalnum():
#             continue
#
#         # 3) at least one vowel
#         has_vowel = any(c in vowels for c in word)
#         # 4) at least one consonant (letters that are not vowels)
#         has_consonant = any(c.isalpha() and c not in vowels for c in word)
#
#         if has_vowel and has_consonant:
#             count += 1
#
#     return count
#
#
# print(countValidWords("This is Form16 submis$ion date"))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# people = [Person("Alice", 30), Person("Bob", 25), Person("Carol", 35)]
# # Sort by age
# people.sort(key=lambda p: p.name)
#
# print([(p.name, p.age) for p in people])

from collections import Counter

s = "prithviraj"

print(Counter(s))
print(Counter(s).most_common(2))
print(list(Counter(s).elements()))