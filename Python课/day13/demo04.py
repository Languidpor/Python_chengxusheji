'''练习，读懂以下程序'''
L = [lambda args:args**2,lambda args:args**3,lambda args:args**4]
for f in L:
    print(f(2))
print(f[1](2))

L = {"1":lambda :1+1,"2":lambda :2+2,"3":lambda :3+3}
print(L["2"]())

def fun(a,b,func):
    return func(a,b)
fun(1,2,lambda x,y:x+y)
fun(1,2,lambda x,y=5:x+y)
#自行查询map函数的意义
print(list(map(lambda x:x*x,list(range(100)))))
