list = []
a = [1,2,3]
name_list=[]
for i in a:
    dict = {}
    b = input('请输入名字')
    d = input('请输入年龄')
    e = input('请输入性别')
    f = input('请输入QQ号')
    g = input('请输入体重')
    if b not in name_list:
        dict['name']=b
        dict['age']=d
        dict.setdefault('sex',e)
        dict['QQ号']=f
        dict['weight']=g
        list.append(dict)
        name_list.append(b)
    else:
        print('名字重复，重新输入')
for j in list:
    print('')
    for n in j:
        print('%s:%s'%(n,j[n]))   
