#接收任意的位置传参，任意的关键字传参
def f5(*agrs,**kwargs):
    pass

'''练习1、写一个函数myrange,此函数返回一个range规则的整数列表
例如 myrange(3)--->[0,1,2]
     myrange(3,6)--->[3,4,5]
     myrange(1,10,3)--->[1,4,7]
     start stop step'''
def myrange(start,stop=None,step=1):
    if stop is None:#用户只传了一个参数x，于是start=0,stop=x
        stop = start
        start = 0
    L = []#生成0~stop之间的整数，步长是step
    i = start
    while i<stop:
        L.append(i)
        i = i+step
    return L
'''   练习2、写一个函数isprime(n),返回boolean，判断n是否为质数，
          写一个函数prime_m2(m,n),返回从m到n之间的所有质数
          写一个函数primes(n)，返回0到n之前的所有质数
'''
def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):#2~n-1
        if n%i==0:
            return False
    return True
def prime_m2(m,n):
    for i in range(m,n+1):
        if isprime(i):
            print(i)
def primes(n):
    prime_m2(0,n)