from collections import Counter

from fontTools.misc.cython import returns

l = [1, 3, 2, 4, 3]
k = 3

freq = Counter(l)

for i in l:
    if freq[i] == 1:
        k -= 1

    if k == 0:
        print(i)
        break


