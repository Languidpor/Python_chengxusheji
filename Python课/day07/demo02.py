'''列表的基本操作'''
L = [1,1,1,1,2,3,4,5]
obj = L.pop()#删除最后一个元素，并返回这个元素
print(obj)
print(L)#[1,1,1,1,2,3,4,]

L.remove(1)
print(L)#[1,1,1,2,3,4]

del L[4]
print(L)#[1,1,1,2,4]

flag = 3 in L#false
print(flag)
flag = 3 not in L#true
print(flag)