#dict = {键:值,键:值,键:值,键:值,键:值}
#以下的字典中包含字符串，整型，布尔型，其键值必须是不可变类型
d1 = {"name":"郭德纲","age":55,"gender":True}
print(d1)

#练习1，测试键值重复时什么情况，None  0，False，True能否作为键来使用
#练习2，字典从创建方式有
# dict()
# dict(可迭代对象)，测试使用可迭代对象去创建一个字典

d2 = dict([("name","张三"),("age",20)])
print(d2)

d3 = dict(name="李四",age=25,score=100)
print(d3)