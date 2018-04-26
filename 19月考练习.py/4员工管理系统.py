list =[]
def print_men():
    print('欢迎来到员工管理系统'.center(30,'&'))
    print('1：录入信息')
    print('2：查询信息')
    print('3：所得工资')
    print('4：删除信息')
    print('5：退出系统')
def change_num():
    while True:
        choose = int(input('请选择功能'))
        if choose == 1:
            add_information()
        elif choose == 2:
            cat_information()
        elif choose == 3:
            pass
        elif choose == 4:
            pass
        elif choose == 5:
            break
def add_information():
    dict={}
    while  True:
        name = input('请输入姓名')
        number = input('请输入工号')
        for temp in list :
            if number == temp['number']:
                print('工号重复，请重新输入')
                break
                continue
        age = input('请输入年龄')
        job = input('亲输入工作岗位')
        money = input('请输入每月薪水')
        date = input('请输入入职日期')
        dict['name'] = name
        dict['number'] = number
        dict['age'] = age
        dict['job'] = job
        dict['money'] = money
        dict['date'] = date
        list.append(dict)
        break
def cat_information():
    num = input('请输入工号')
    for temp in list:
        if num == temp['number']:
            for j in temp:
                print('%s:%s'%(j,temp[j]))
def money_information():
   pass 
print_men()
change_num()
