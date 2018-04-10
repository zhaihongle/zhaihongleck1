list = []#设置一个新列
name_list = []#设置一个新放所有输入过的信息
count = 0 #输入次数
while True:
    if count ==3:
        break
    dict = {}
    name = input("输入名字")
    age =int( input("输入年龄"))
    sex = input("输入性别")
    qq = input("输入qq")
    weight = input("输入体重")
    if name not in name_list :
        dict['name']=name
        dict['age']=age
        dict['sex']=sex
        dict['qq']=qq
        dict['weight']=weight
        list.append(dict)
        name_list.append(name)#讲输入过的名字放进去
        print(list)
        count+=1
    else:
        print('名字重复')
age_sum = 0
for i in list:
    age_sum = age_sum+i.get("age")
print("年龄平均只是%d"%(age_sum/len(list)))

    
        
