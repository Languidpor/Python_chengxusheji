'''练习
1、用程序输出
      *
    ***
  *****
*******
2、古代的称16两一斤，请问216两是几斤几两
3、从凌晨00：00：00计算，经过了63320秒后是几时几分几秒
'''
print(" "*5,end="")
print("*")
print(" "*3,end="")
print("*"*3)

# /除   //地板除 商   %取余
total_weight = 216
unit_weight = 16

jin = total_weight//unit_weight
liang = total_weight%unit_weight

print(total_weight,"两，在古代是：",jin,"斤",liang,"两")

total_seconds = 63320
hours = total_seconds//3600
minutes = total_seconds%3600//60
seconds = total_seconds%3600%60
print(total_seconds,"秒是",hours,"时:",minutes,"分:",seconds,"秒")