#格式化字符串
print("%-10d" % 123)#左对齐
print("%10d" % 123)#右对齐
print("%+5d" % -123)#显示正负符合
print("%06d" % 456)
print("%7.3f" % 3.1415926) #  3.142

print("%-5d,%3d" % (123,456))
#练习：输入三行文字，
# 让这些文字依次以总长度20右对齐输出
# 以最长的那个字符串进行右对齐
'''
          hello world
                 abcd
                nihao
'''
str1 = input("请输入第一段文本")
str2 = input("请输入第二段文本")
str3 = input("请输入第三段文本")
#print("%20s" % str1)
#print("%20s" % str2)
#print("%20s" % str3)
m = max(len(str1),len(str2),len(str3))
print("最大长度",m)
print(" "*(m-len(str1))+str1)
print(" "*(m-len(str2))+str2)
print(" "*(m-len(str3))+str3)


