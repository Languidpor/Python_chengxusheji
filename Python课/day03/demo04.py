#练习：1 今天是小明20岁生日，计算他过了多少星期，假设每年都是365天
#      2 分三次输入当前的时分秒，程序计算距离今天凌晨一共过了多少秒
days = 20*365
weeks = days//7
day = days%7
print(weeks,day)

hours = int(input("请输入当前 时"))
minutes = int(input("请输入当前 分"))
seconds = int(input("请输入当前 秒"))
total_seconds = hours*3600 + minutes*60 + seconds
print(total_seconds)