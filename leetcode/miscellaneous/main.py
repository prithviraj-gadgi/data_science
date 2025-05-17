from datetime import datetime

def convert_date(yymmdd):
    date_obj = datetime.strptime(yymmdd, "%y%m%d")
    return date_obj.strftime("%d%m%y")

print(convert_date("250510"))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b


fibonacci(10)