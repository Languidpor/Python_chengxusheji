'''高阶函数filter'''

#练习1：筛出1~20之间的偶数
for i in filter(lambda x:x%2==0,range(1,21)):
    print(i)
print("~~~~~~~~~")
#练习2：筛选出1~1000之内的素数，组成列表返回，使用列表推导式
def isprime(n):
    for i in range(2,n):
        if n%2==0:
            return False
    return True
L = [x for x in filter(isprime,range(2,1001))]
print(L)