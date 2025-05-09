"“%[(keynames)[flags][width][.precision]]typecode“ % (values)"

print("%(id)s and %(name)s" % {"id":"1001","name":"zhangsan"})
x = 1.23456789
print("%-6.2f,%+3.4f,%06.9f,% 6.2f" % (x,x,x,x))

print("%s and %*.*f" % ("abc",3,5,7.777777777))