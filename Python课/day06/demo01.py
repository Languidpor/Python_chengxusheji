'''字符串的其他常用操作'''
# str.find(“”) 查找是否包括子字符串，返回索引，否则返回-1
str1 = "32$675.99"
print(str1.find("$"))
print(str1.find("."))
print(str1.find("12"))
# str.rfind(“”),从右往前查找
# str.index(“”)，也是查找，只是找不到会报错
# str.rindex(“”)，从右往前
# str.count(“”)#查找子字符串出现的次数
# str.replace(“”,””)替换，后面的参数替换前面的参数
# str.replace(“”,””,1)替换，指定了替换的次数

# str.split() 默认按照空格进行分割，返回一个列表
str1 = "abcde"
str2 = "ab c d    e"
print(str1.split())
print(str2.split())
# str.split(“”)按照指定的字符串进行分隔
str1 = "sajkahasakadajafh";print(str1.split("a"))
str2 = "sabjkahabsakabdabjafh";print(str2.split("ab"))
str3 = "[清] 曹雪芹 著 / 人民文学出版社 / 1996-12 / 59.70元"
print(str3.split("/"))
# str.capitalize()第一个字母大写
str1 = "i am guojk"
str2 = "iamguojk"
str3= "i amguojk"
print(str1.capitalize())
print(str2.capitalize())
print(str3.capitalize())
# str.title()每一个单词的首字母都大写, , \n
str4 = "i,am,guojk"
str5 = "i\nam,guojk\nnihao"
print(str1.title())
print(str2.title())
print(str3.title())
print(str4.title())
print(str5.title())
# str.endswith(“”)判断是否以某字符串结尾
# str.startswith(“”)判断是否以某字符串开始
# str.lower()全部变成小写
# str.upper()全部变成大写
# str.center(width)，把字符串居中，一共的长度是width，左右补空格
# str.ljust(width)靠左对其 右补空格
# str.rjust(width)靠右对其 左补空格
# str.strip() 去掉所有空格
# str.rtrip() 去掉右边空格
# str.ltrip() 去点左空格
