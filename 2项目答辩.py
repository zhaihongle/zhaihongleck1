list = []
def interface():
    print('欢迎来到请假系统'.center(30,"*"))
    print('1-入学功能'.center(20," "))
    print('2-请假功能'.center(20," "))
    print('3-消假功能'.center(20," "))
    print('4-退学功能'.center(20," "))
    print('5-关闭系统'.center(20," "))
def change():
    while True:
        choose_num = int( input('请选择功能'))
        if choose_num == 1:
            add_num()
        if choose_num == 2:
            go_class()
        if choose_num == 3:
            return_school()
        if choose_num == 4:
            leave_school()
        if choose_num == 5:
            print('退出系统')
            break
def add_num():
    while True:
            dict = {}
            name = input ('请输入学生名字：')
            sleep = input('请输入是否住宿')
            if sleep != '是' and sleep != '否':
                print('输入有误，请输入是或否')
                continue
            sex = input('请输入性别')
            if sex != '男' and sex != '女':
                print('输入有误，请输入男或女')
                continue
            f_name =input ('请输入家长姓名')
            def check_phone():
                if phone.startswith('1') and len(phone) == 11: 
                    return True
                else:
                   return False
            phone = input('请输入家长电话')
            check = check_phone()
            if check == False:
                print('输入有误')
                continue
            dict['name']=name
            dict['sleep']=sleep
            dict['sex']=sex
            dict['f_name']=f_name
            dict['phone']=phone
            dict['please']='否'
            list.append(dict)
            print('恭喜你成为王者荣耀小学的一员\n')
            break
def go_class():        
        name = input ('请输入你的名字')
        flag = False
        for temp in list:
            if name == temp['name']:
                flag = True 
                temp['please'] = '是'
                print('你是本校学生，可以离校')
                print('')
                break
        if flag == False:
            print('你输入的名字不是本校学生，不能离校\n')
def return_school():
    name = input ('请输入名字')
    please = input ('是否请过假')
    if please != '是':
        print('输入有误，如果你已经请假，请输入中文“是”')
    for i in list:
        if name == i['name'] and please == i['please']:
            i['please']='否'
            print('可以返校\n')
        else:
            print('不是本校学生')
def leave_school():
        name = input('请输入名字')
        for i in list:
            if name == i['name']:
                print('允许退学\n')
                print(list)
interface()
change()
