#定义函数装饰器
def mydeco(fn):
    def fx(name):
        print("开始问候")
        fn(name)
        print("结束问候")
    return fx
@mydeco
def say(name):
    print("你好：",name)
say("郭德纲")

