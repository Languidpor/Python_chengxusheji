def f1(*args,d,e):
    print("args=",args)
    print("d=",d)
    print("e=",e)
#f1(1,2,d=3,e=4)#没问题
# *前面的形参是0个或多个，*号后面的形参是1个或多个
def f2(a,*,b):
    print("a=",a)
    print("b=",b)

f2(a=1,b=2)
f2(1,**{"b":3})

'''双星号字典形参'''
def f3(**kwargs):
    print(kwargs)
f3()
f3(name="张三",age=12)
#f3(1,2,3)

#a,b 位置形参            关键字传参或者位置传参
#*args 星号元组形参      把传来的值以元组存储，位置传参
#c 命名关键字形参        关键字传参
#**kwargs 双星号字典形参  关键字传参
def f4(a,b,*args,c,**kwargs):
  pass
f4(a=1,b=2,*[3,4,5,6,7],c=8,name="zz",age=20,gender="男")
#思考以下函数的意义
def f5(*agrs,**kwargs):
    pass
'''练习1、写一个函数myrange,此函数返回一个range规则的整数列表
例如 myrange(3)--->[0,1,2]
     myrange(3,6)--->[3,4,5]
     myrange(1,10,3)--->[1,4,7] 
   练习2、写一个函数isprime(n),返回boolean，判断n是否为质数，
          写一个函数prime_m2(m,n),返回从m到n之间的所有质数
          写一个函数primes(n)，返回0到n之前的所有质数
'''



