'''
3、完全数，6=1+2+3，
求100000以内的所有完全数 28=1+2+4+7+14
'''
#等一个函数，接收一个参数，返回一个boolean
def is_perfect(n):
    #得到n的所有的因子(不包括本身)，这些因子求和值
    L = []
    for i in range(1,n):
        if n%i==0:
            L.append(i)
    if sum(L)==n:
        return True
    return False

for i in range(1,100000):
    if is_perfect(i):
        print(i)