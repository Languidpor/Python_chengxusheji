import sys,os,math,random,time
#查看这些模块的相关属性，模块的文档字符串
#练习1，使用math模块提供的相关函数完成以下任务
#math.pow(x,y[,z]) 返回x的y次方，如果有z，会对z取余
#math.pi 圆周率
#math.sqrt(x),对x开平方

#1、输入一个正方形的周长，输出此正方形的面积
length = float(input("请输入正方形的周长"))
area = math.pow(length/4,2)

#2、输入一个圆的半径，输出这个圆的面积
r = float(input("请输入一个圆的半径"))
area = math.pi*r*r

#3、输入一个正方形的面积，输出此正方形的周长
area = float(input("请输入正方形的面积"))
lenght = math.sqrt(area)*4
