
def make_power(y):
    def fx(args):
        return args**y
    return fx

f = make_power(2)#调用此外部函数，会返回一个函数的引用

print(f(5))#5的2次方,在此处相当于访问了外部函数的那个局部变量

def f1(y):
    print(y)
f1(3)