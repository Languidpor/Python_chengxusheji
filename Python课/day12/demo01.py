'''函数的形参缺省值'''
def info(name,age=1,address="北京市"):
    print(name,"今年",age,"岁，家庭住址是:",address)

info("郭德纲")
info("郭麒麟",20)
info("于谦",40,"河北省")
#练习：定义一个函数，可以接收三个参数，也可以接收两个参数
#当接收两个参数的时候，返回这两个参数的和值
#当接收三个参数的时候，返回前两个参数的和值对第三个数取余的结果
def myfun(a,b,c=None):
    if c is None:
        return a+b
    return (a+b)%c

'''星号元组形参'''
def fun(*args):
    print("和值:",sum(args))
    print("个数:",len(args))

fun(1,2,3,4,6)
fun()
fun(1)
fun(*[1,2,3,4])#序列传参，其本质是位置传参


'''命名关键字形参'''
