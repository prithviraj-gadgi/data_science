"""
  Time complexity: O(n^2)
  Space complexity: O(1)
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [2, 1, 3]
bubble_sort(arr)
print(arr)
