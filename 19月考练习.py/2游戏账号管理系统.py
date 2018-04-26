list =[]
list1 = []
def print_men():
    print('1：注册')
    print('2：登录')
    print('3：退出')
    while True:
        choose = input('请选择功能')
        if choose == '1':
            come()
        elif choose == '2':
            comeon()
        elif choose == '3':
            break

def come():
    while True:
        print('账号注册')
        account = input ('请输入账号')
        if account in list:
            print('该账户已经注册\n')
            continue
        else:
            print('注册成功\n')
        list.append(account)
        break
def comeon():
    
    print('账户登录')
    account = input('请输入账号')

    if account in list1:
        print('该账号已经登录过\n')
    else :
        print('登录成功\n')
        list1.append(account)

print_men()

