'''
技术人员：{"曹操","刘备","张飞","赵云"}
经理：{"曹操"，"刘备","周瑜"}
1、既是经理又是技术人员
2、是经理，但不是技术人员
3、是技术人员，但不是经理
4、张飞是不是经理
5、身兼一职的有哪些
6、经理和技术人员一共有多少
'''
A = {"曹操","刘备","张飞","赵云"}#技术人员
B = {"曹操","刘备","周瑜"}#经理
# 1、既是经理又是技术人员
print("既是经理又是技术人员",A&B)
# 2、是经理，但不是技术人员
print("是经理，但不是技术人员",B-A)
# 3、是技术人员，但不是经理
print("是技术人员，但不是经理",A-B)
# 4、张飞是不是经理
if "张飞" in B:
    print('张飞是经理')
else:
    print('张飞不是经理')
# 5、身兼一职的有哪些
print("身兼一职的有",A^B)
# 6、经理和技术人员一共有多少
print("经理和技术人员一共有%d个人"%len(A|B))




frozenset




