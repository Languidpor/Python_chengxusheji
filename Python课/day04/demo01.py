#九九乘法表
'''
1*1=1
1*2=2 2*2=4
'''
i=1
while i<=9:#控制每一行
    j = 1
    while j<=i:#控制每一行具体做什么
        print("%d*%d=%d "%(i,j,i*j),end="")
        j+=1
    print()
    i+=1





