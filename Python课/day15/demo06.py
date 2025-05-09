#模拟银行取钱存钱系统，在每一个操作之前都做一些提示
#定义函数装饰器
def message_send(fn):
    def fx(name,x):
        print("发送消息",name,"来办理业务")
        fn(name,x)
        print("发送消息",name,"办理了",x,"业务")
    return fx
@message_send
def savemoney(name,x):
    print(name,"存钱",x,"元")
savemoney("张三",1000)



