accout = input("请输入账号")
pwd = input('请输入密码')

count=1
if accout == 'cuijian' and pwd == '123456':
    print("登陆成功")
    o = input('请选择英雄职业:0=ADC 1=肉 3=法师')
    if o =='0':
        print("鲁班大师")
    elif o =='1':
        print("程咬金")
    elif o =='3':
        print("王昭君")
else:
    while count <=3:
        accout = input("请重新输入账号")
        pwd = input("请重新输入密码")
        count+=1
    print("账号冻结")

   


