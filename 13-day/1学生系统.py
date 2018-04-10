print('欢迎来到王者荣耀小学编辑系统'.center(30,"*"))
print('1-入学功能'.center(20," "))
print('2-请假功能'.center(20," "))
print('3-消假功能'.center(20," "))
print('4-退学功能'.center(20," "))
print('5-关闭系统'.center(20," "))
list = []
while True:
    choose_num = int( input('请选择功能'))
    if choose_num == 1:
        dict = {}
        name = input ('请输入学生名字：')
        sleep = input('请输入是否住宿')
        sex = input('请输入性别')
        f_name = input ('请输入家长姓名')
        phone = input('请输入家长电话')
        dict['name']=name
        dict['sleep']=sleep
        dict['sex']=sex
        dict['f_name']=f_name
        dict['phone']=phone
        list.append(dict)
        print('恭喜你成为王者荣耀小学的一员\n')

    if choose_num == 2:
        dict1 = {}
        name = input ('请输入你的名字')
        flag = False
        for temp in list:
            if name == temp['name']:
                flag = True 
                print('你是本校学生，可以离校')
                time = input('请输入离校时间')
                return_time = input('请输入返校时间')
                print('')
                dict1['name'] = name 
                dict1['time'] = time
                dict1['return_time'] = return_time
                list.append(dict1)
                s_num = list.index(dict1)
                break
            elif name == list[s_num]['name']:
                print('该学生以经请假，无法再次请假\n')
        if flag == False:
            print('你输入的名字不是本校学生，不能离校\n')
           
            continue
    if choose_num == 3:
        name = input ('请输入名字')
        s_num = list.index(dict1)
        if name == list[s_num]['name']:
            print('可以返校\n')
        else:
            print('你不是本校学生\n')
    if choose_num == 4:
        name = input('请输入名字')
        #for i in list.index(dict)
        s_num = list.index(dict)
        if name == list[s_num]['name']:
            print('允许退学\n')
            #list.remove('name')
    if choose_num == 5:
        print('退出系统')
        break



