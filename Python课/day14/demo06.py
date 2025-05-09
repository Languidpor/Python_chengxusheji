'''高阶函数sorted'''
L1 = [5,-1,2,10,3,6,-2]
L2 = ["aa","zz","bb","ls","ww","zl"]
d = [{"name":"张三","age":21},
     {"name":"李四","age":19},
     {"name":"王五","age":20}]
print(sorted(L1))
print(sorted(L2))

print(sorted(d,key=lambda x:x["age"]))

