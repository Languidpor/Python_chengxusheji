'''高阶函数map'''

def pow2(n):
    return n**2

for i in map(pow2,range(1,11)):
    print(i)
print("!!!!!!!!!!")

def pow3(x,y):
    return x+y
for i in map(pow3,range(1,11),[4,5,6,7]):
    print(i)
# 重写练习3：写一个函数power_sum(n),计算1+2**2+3**3+...+n**n的和值
def power_sum(n):
    return sum(map(lambda x:x**x,range(1,n+1)))
#练习 计算1**9+2**8+3**7+...+9**1 的和值
#提示 pow(x,y,z=None)，此函数是python提供的，计算x的y次方
#若z提供，则再对z取余
print(sum(map(pow,range(1,10),range(9,0,-1))))


