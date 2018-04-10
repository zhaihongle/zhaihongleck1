print('欢迎来到名片系统'.center(30,"*"))
print('请选择功能'.center(20,' '))
print('1：新增名片'.center(20,' '))
print('2：查找名片'.center(20,' '))
print('3：删除名片'.center(20,' '))
print('4：更改名片'.center(20,' '))
print('5：退出系统'.center(20,' '))
cards = []
while True:    
    fun_number = int(input('请选择功能\n'))
    if fun_number == 1:
        card = {}
        flag = False
        name = input('请输入名字')
        for temp in cards:   #判断重复 14行到20行 
            if name == temp['名字']:
                flag = True
                break   #跳出for循环
        if flag == True:
            print('名字重复，请重新输入')
            continue    #继续while循环
        phone = int(input('请输入手机号'))
        job= input('请输入职位')
        company= input('请输入公司名字')
        address = input('请输入公司地址')
        card['名字']=name
        card['手机号']=phone
        card['职位']=job
        card['公司']=company
        card['地址']=address
        cards.append(card)
        print('添加成功\n')
    elif fun_number == 2:
        name = input('请输入要查找的名字') 
        flag = False#假如不在里面
        for temp in cards:
            if name == temp['名字']:
                flag=True#找到
                for c in temp:
                    print('%s:%s\n'%(c,temp[c]))
                break
        if flag == False:
            print('查无此人\n')
            
    elif fun_number == 3:
        name = input('请输入删除的名字')
        flag=False
        for temp in cards:
            if name ==temp['名字']:
                flag=True
                sure_num = int(input('0确认删除 1返回\n'))
                if sure_num == 0:
                    cards.remove(temp)
                    print('删除成功\n')
                break
        if flag == False:
            print('没有此人\n')
                 
    elif fun_number == 4:
        pass
    elif fun_number == 5:
        break
