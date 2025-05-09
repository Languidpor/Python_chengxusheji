def f1():
    print("f1函数被调用")

def f2(n):
    n()

def f3():
    print("f3函数被调用")

f1,f3 = f3,f1
f1()


def fx(a,fn):
    return fn(a)
L = [3,56,7,2,76,9,0,0,2,23]
fx(L,sum)#sum是一个变量，绑定了Python提供的那个内置函数
fx(L,min)
fx(L,max)
#一个函数中返回另一个函数,用户输入
# 1 + 1   1 - 1   1 * 1   1 / 1,程序给出结果
# 定义四个小函数，分别表示以上四个操作
# 再定义一个函数，根据用户输入的内容，分别返回以上四个函数的函数名
def myadd(a,b):
    return a+b
def mysub(a,b):
    return a-b
def mymul(a,b):
    return a*b
def myfn(a,b):
    return a/b

def get_op(s):# + - * /
    if s == "+":
        return myadd
    if s == "-":
        return mysub
    if s == "*":
        return mymul
    if s == "/":
        return myfn

def main():
    str = input("请输入计算内容")
    L = str.split()
    f = get_op(L[1])
    result = f(int(L[0]),int(L[2]))
    print(result)
main()




