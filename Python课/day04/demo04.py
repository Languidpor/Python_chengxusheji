'''字符串比较'''

print('A'>'B')#False
print("ABC">"AB")#True
print("AD"<"ABC")#False
print("ABC"=="abc")#False

s = "welcome to yangzhou"
print("to" in s)


str = "ABCDE"
a = str[1:4]#BCD
a = str[1:]#BCDE
a = str[:2]#AB
a = str[:]#ABCDE
a = str[4:2]# ""
a = str[2:10000]#切到尾部

a = str[::2]
a = str[1::2]
a = str[::-1]
a = str[::-2]
a = str[4:0:-2]
#1写一个程序，输入一个字符串，把字符串的最后一个和
#第一个字符去掉后，输出出来
#2写一个程序，输入一个字符串，判断是不是回文