def update_age():
    age=int(input('请输入年龄'))
    if age < 2:
        print('你是婴儿')
    elif age >= 2 and age < 13:
        print('你是儿童，可以参加儿童节') 
    elif age >=13  and age < 20:
        print('你是青少年')
    elif age >=20 and age < 65:
        print('你是成年人')




update_age()
