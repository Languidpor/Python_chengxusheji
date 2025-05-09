'''全局变量和局部变量'''
a = 1
def f1():
    global a
    a = 2
    print(a)

f1()

print(a)


L = [1,2,3]
dic = {"name":"张三","age":20}
def f2():
    #修改字典或列表的元素的内容
    # L.append(4)
    # dic["age"] = 21
    #修改整个字典或列表
    L = [4,5,6]
    dic = {"id":1001}
f2()
print(L)
print(dic)
