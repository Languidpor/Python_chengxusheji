'''匿名函数'''
#列表的排序
L1 = [2,3,4,7,9,0,1]
L2 = ["郭德纲","于谦","岳云鹏","郭麒麟"]
L3 = [4,3,2,"张三","李四"]

L4 = [{"name":"lisi","age":23},
      {"name":"zhangsan","age":21},
      {"name":"wangwu","age":22}]

L4.sort(key=lambda x:x["age"])

print(L4)
#匿名函数也是可以绑定在一个变量中的
f1 = lambda a,b:a+b
f1(1,2)
#练习，"nihao my name is guodegang \nand you\t?"
str = "nihao my name is guodegang \nand you\t?"
#nihaomynameisguodegangandyou?
print(str)
f=lambda s:"".join(s.split())
print(f(str))


