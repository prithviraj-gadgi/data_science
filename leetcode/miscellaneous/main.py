# import pandas as pd
#
# def convert_date(date):
#     date_obj = pd.to_datetime(date, format="%Y-%b-%d")
#     print(f"{date_obj:%d/%m/%Y}")
#     return date_obj.strftime("%d-%m-%Y, %A, %a, %b, %B")
#
# print(convert_date("2025-Jun-10"))


# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a+b
#
# fibonacci(10)
#
#
import math
from collections import Counter

def calculateMinProcessingSteps(transactionLedger: str) -> int:
    freq = Counter(transactionLedger)
    print(freq)
    return sum(math.floor(k/2) for k in freq.values())

print(calculateMinProcessingSteps('baabacaa'))


# with open(file='test.txt', mode='w+') as f:
#     f.write("This is my first line.\nThis is my second line.")
#
# with open(file='test.txt', mode='r+') as f:
#     print(f.read())
#     f.seek(0)
#     print(f.readline())
#     f.seek(0)
#     print(f.readlines())