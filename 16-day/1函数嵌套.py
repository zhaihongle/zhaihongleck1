def login (phone,pwd):
    reslut = isphone(phone)
    import random
    vv=random.randint(1,10)
    print(vv)
    xx = int(input('验证码'))
    if xx == vv:
        if reslut ==True:
            print('成功')
        elif reslut == False:
            print('失败')


def denglu (phone,pwd):
    reslut = isphone(phone)
    if reslut :     #可以加True
        print('登录')
    else:          #可以加False
        print('登事')
def isphone(phone):
    if phone.startswith('1') and len(phone)==11:
        return  True
    else:
        return False


phone=input('手机号')
pwd=input('密码')
login(phone,pwd)
denglu(phone,pwd)
