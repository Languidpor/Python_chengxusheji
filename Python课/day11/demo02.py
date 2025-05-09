'''
1、写一个函数，此函数显示两个参数的相关信息：
最大值、和值、乘积，从第一个数到第二个数之间所有的偶数
'''
def myfun(a,b):
    #打印最大值
    print("最大值是：",max(a,b))
    #打印和值
    print("和值",a+b)
    #乘积
    print("乘积",a*b)
    #第一个数到第二个数之间所有的偶数
    max1 = max(a,b)
    min1 = min(a,b)
    for x in range(min1,max1+1):
        if x%2==0:
            print(x,end=",")
myfun(2,10)



