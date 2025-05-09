'''集合'''
#创建集合
s = {1,2,3}#创建非空集合
s = set()#创建空集合
#使用可迭代对象创建非空集合
str = "abcd"
L = [1,2,2,3,3,4,5,7,8,9,0]
t = (4,65,7,87,9,9,6,4,43,4,4)
s = set(str)
s = set(L)
s = set(t)

#集合的元素都要求是不可变类型，为什么

L1 = ['zhangsan'] #列表是可变类型
L2 = ['zhangsan']
s = {2,3,4}
s.add(5)

obj = s.pop()
print(obj)
print(s)

s = set("abcd")
# obj = s.pop()
# print(obj)
# print(s)

