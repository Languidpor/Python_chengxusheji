# 练习1，一个商店卖西瓜7元一个，你带20块钱能买几个西瓜，找零多少钱
price = 7
user_money = 20
count = user_money//price #地板除，求商
change_money = user_money%price #取余
print("卖西瓜个数:",count,"找零:",change_money)

#练习2，一个学生毕业的薪资是10000元，每年涨薪20%，十年后的薪资是多少
salary = 10000
add = 0.2
salary = salary * 1.2**9
print(salary)

