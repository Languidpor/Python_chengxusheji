def fx(n):
    print("程序进入，第",n,"层")
    if n==3:
        return
    fx(n+1)
    print("程序退出，第",n,"层")
#fx(1)
# 练习1、1+2+3+…+100的和值
def mysum(n):
    if n==1:
        return 1
    return n + mysum(n-1)
print(mysum(100))

# 练习2、求n的阶乘
def myfac(n):
    if n==1:
        return 1
    return n * myfac(n-1)
print(myfac(5))