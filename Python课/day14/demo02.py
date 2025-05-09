def mysum(n):#练习1：写一个函数mysum（n），计算1+2+3...+n的和值
    return sum(range(1,n+1))
def myfac(n):#练习2：写一个函数myfac(n),计算n的阶乘
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
def myfac(n):#练习3：写一个函数power_sum(n),计算1+2**2+3**3+...+n**n的和值
    s = 1
    for i in range(1,n+1):
        s += i**i
    return s