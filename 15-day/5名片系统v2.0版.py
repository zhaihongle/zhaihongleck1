cards = []
def interface():
    print("欢迎来到名片系统v2.0".center(30,"$"))
    print("1:增加名片".center(30," "))
    print("2:查找名片".center(30," "))
    print("3:删除名片".center(30," "))
    print("4:修改名片".center(30," "))
    print("5:打印名片".center(30," "))
    print("6:退出系统".center(30," "))
def input_fun():
    while True:
        choose_num =int(input("请选择功能"))
        if choose_num == 1:
            add_card()
        elif choose_num == 2:
            find_card()
        elif choose_num == 3:
            del_card()
        elif choose_num == 4:
            change_card()
        elif choose_num == 5:
            all_card()
        else:
            break
def add_card():
    card = {}
    name = input("名字")
    job = input("职位")
    phone = input("手机号")
    company = input("公司")
    card['name'] = name
    card['job'] = job
    card['phone'] = phone
    card['company'] = company
    cards.append(card)
    print("新增成功")
def find_card():
    name = input("名字")
    flag = False
    for temp in cards:
        if name == temp['name']:
            flag = True
            for i in temp:
                print('%s:%s'%(i,temp[i]))
            print('ok')
        if flag == False:
            print('no baby')
    if flag == False:
        print('no baby')
def del_card():
    name = input("名字")
    flag = False
    for temp in cards:
        if name == temp['name']:
            flag = True
            cards.remove(temp)
            print('ojbk')
    if flag == False:
        print('nobody')
def change_card():
    name = input("你确定的细心")
    flag = False
    for  temp in cards:
        if name == temp['name']  or name == temp['job'] or name== temp['phone'] or name == temp['company'] :
            flalg = True
            print('1:改名字')      
            print('2:改职位')      
            print('3:改手机号')      
            print('4:改公司')
            ss_num = int(input('修改选项'))
            if ss_num == 1 :
                new_name = input('new name')
                temp['name'] = new_name     
            if ss_num == 2 :
                new_job = input('new job')
                temp['job'] = new_job   
            if ss_num == 3 :
                new_phone= input('new phone')
                temp['phone'] = new_phone     
            if ss_num == 4 :
                new_company = input('new company')
                temp['compy'] = new_company 
            else:
                print('NONONO')    
    if flag == False:
        print('NONONO')    
def all_card():
    for temp in cards:
        for i in temp:
            print('%s:%s'%(i,temp[i]))

interface()
input_fun()
