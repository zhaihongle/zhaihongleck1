list = []   
def big_function():
    print('学生成绩管理系统'.center(30,'￥'))
    print('1:录入成绩'.center(30,' '))
    print('2:查询成绩'.center(30,' '))
    print('3:修改成绩'.center(30,' '))
    print('4:删除成绩'.center(30,' '))
    print('5:打印成绩'.center(30,' '))
    print('6:退出系统'.center(30,' '))
def input_function():
    while True:
        choose = int(input('请选择功能'))
        if choose == 1:
            add_card()
        elif choose == 2:
            find_card()
        elif choose == 3:
            update_card()
        elif choose == 4:
            del_card()
        elif choose == 5:
            for temp in list:
                for i in temp :
                    print('%s:%s'%(i,temp[i]))

        else:
            break
"""
def yong ():
    flag = False
    num = int(input('学号'))
    for temp in list:
        if num == temp['number']:
            flag = True
"""
def add_card():
    while True:
        dict = {}
        flag = False
        name = input('名字')
        number = int(input('学号'))
        for temp in list:
            if number == temp['number']:
                flag = True
                break
        if flag == True:
            print('序号重复')
            continue
        subject = input('科目')
        score = input('成绩')
        dict['name'] = name
        dict['number'] = number
        dict['subject'] = subject
        dict['score'] = score
        list.append(dict)
        break
def find_card():
    num = int(input('学号'))
    flag = False
    for temp in list:
        if num == temp['number']:
            flag = True
            for i in temp:
               print('%s:%s'%(i,temp[i]))
    if flag == False:
        print('nobody')
def update_card():
    num = int(input('学号'))
    flag = False
    for temp in list:
        if num == temp['number']:
            flag = True
            new_score = input('请输入新的成绩')
            temp['score'] = new_score
    if flag == False:
        print('nobody')
def del_card():
    num = int(input('学号'))
    flag = False
    for temp in list:
        if num == temp['number']:
            flag = True
            sure = input('1-确定 2-返回')
            if sure == 1:
                temp.pop('score')
            else :
                break
    if flag == False:
        print('nobody')
big_function()
input_function()
