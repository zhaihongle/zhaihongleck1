account = input('请输入账户')
passwd = input("请输入密码")
name = input("请输入你的名字")
money = 20000
need_money = input("请输入您要提前的金额")
sum = money - int(need_money)
print("账号:%s\n密码%s\n姓名:%s\n原有存款为:%s\n取款金额:%s\n剩余为:%s"%(account,passwd,name,money,need_money,sum))
