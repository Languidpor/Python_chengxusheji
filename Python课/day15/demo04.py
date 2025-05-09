# 练习：type(x)返回变量/对象的类型
# 例如  type([1,2,3]) is list 返回True
#已知有列表 L = [【3，5，8】，10，【1，23，【3，2】】，5，【6】]
#写一个函数，返回所有的元素
L = [[3,5,8],10,[1,23,[3,2]],5,[6]]
def print_list(l):
    for x in l:
        if type(x) is list:
            print_list(x)
        else:
            print(x)
print_list(L)
