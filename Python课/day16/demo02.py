from math import *
import time
#练习1，输入出生日期,(2002,5,7,0,0,0,0,0,0)计算活了多少秒
#计算活了多少天，计算出生日的星期，出生那天在当年是第多少天
# year = int(input("请输入年份"))
# month = int(input("请输入月"))
# day = int(input("请输入日"))
# t = (year,month,day,0,0,0,0,0,0,)
# seconds = time.mktime(t)
# #print(seconds)
# t = time.localtime(seconds)
# print(t)
#练习2：写一个程序，以电子时钟的方式不停的打印时间，HH:MM:SS
#思路：得到当前时间，转换成时间元组，对元组进行切片得到时分秒
# while True:
#     current_seconds = time.time()
#     current_t = time.localtime(current_seconds)
#     t = current_t[3:6]
#     print(t[0],":",t[1],":",t[2])
#     time.sleep(1)
#练习3，写一个程序，输入时间，到了这个时间时，程序输出一句话，
#然后程序结束
#思路：写一个死循环，不停的判断是否到了这个时间，如果到了就break
hour = int(input("请输入时"))
min = int(input("请输入分"))
while True:
    t = time.localtime(time.time())[3:5]#得到当前时间的时间元组，切片，切出时和分钟
    if (hour,min)==t:
        break
print("时间到")


