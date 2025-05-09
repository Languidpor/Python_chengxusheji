#1、用for循环打印1—20的整数，打印在一行
for i in range(1,21):
    print(i,end=",")

#2、求100以内有哪些整数与自身+1的乘积再对11取余结果等于8
for i in range(1,100):
    if i*(i+1)%11 == 8:
        print(i)




