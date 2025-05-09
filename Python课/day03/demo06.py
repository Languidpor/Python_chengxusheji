#用户输入一个分数，程序判断等级，并输出等级
'''A 90~100
   B 80~89
   C 70~79
   D 60~69
   E 0~59
'''
score = int(input("请输入一个分数"))
if score>=90 & score<=100:
    print("A")
elif score>=80 and score<=89:
    print("B")
elif score>=70 and score<=79:
    print("C")
elif score>=60 and score<=69:
    print("D")
else:
    print("E")




