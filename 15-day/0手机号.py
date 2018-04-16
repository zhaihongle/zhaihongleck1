def check_phone(phone):
    if phone.startswith ('1') and len(phone)==11:
        return True
    else :
        return False

phone = input('请输入手机号')
check= check_phone(phone)
if check == False:
    print('输入有误')
