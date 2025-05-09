def say_hello(name):
    print("hello:",name)


def f1():
    print("f1")

def f2():
    print("f2")
    return "abc"


print(f1())
print(f2())

def get_max(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "两个数一样大"
print(get_max(2,4))


def test1():
    print("111")
    test2()
    print("2222")

def test2():
    print("test2")

test1()