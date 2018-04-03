account  = "翟宏乐"#这是服务器账号
pwd = "123456"#服务器密码
v = 1
a = input("请输入你的名字")
p = input("请输入密码")
if a == account and p == pwd:
    print("登录成功")
    x =int(input("请选择英雄范围 0-ADC 1-肉 3-法"))
    if x == 0:
        print('鲁班')
    elif x== 1:
        print('程咬金')
    elif x == 3:
        print('王昭君')
else:
    while v <= 2:
        a = input('请输入你的名字')
        p = input('请输入密码')
        v+=1
    print('账号冻结')
