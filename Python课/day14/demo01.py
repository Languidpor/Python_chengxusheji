"案例"
x = 100;y = 200
s = "print(x,y,x+y)"
s1 = "x+y"
exec(s)#100,200,300,没有提供globals和locals，会从当前空间查找
exec(s,{"x":10,"y":20})#10，20，30提供了globals
exec(s,{"x":10},{"x":1,"y":2})#1 2 3 globals和locals都提供了，优先locals
exec(s,{"x":1},{"y":2})#1 2 3 globals和locals都提供了

#练习1：写一个函数mysum（n），计算1+2+3...+n的和值
#练习2：写一个函数myfac(n),计算n的阶乘
#练习3：写一个函数power_sum(n),计算1+2**2+3**3+...+n**n的和值


