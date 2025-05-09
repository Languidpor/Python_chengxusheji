
#用户输入商品的单价，购买的数量，用户交了多少钱，程序计算
#总价以及找零多少
price = float(input("请输入商品的单价，必须是数值类型："))
count = int(input("请输入购买的数量，必须是数值类型："))
user_money = float(input("请输入你的总金额，必须是数值类型："))

total_money = price*count # 商品总价
change_money = user_money - total_money# 找零
print("总价：",total_money,"找零",change_money)




