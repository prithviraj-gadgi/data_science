# l = [('Bob', 20), ('Alice', 30), ('Alice', 10)]
#
# l.sort(key=lambda x: (x[0], x[1]))
#
# print(l)

def simple_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello")

say_hello()