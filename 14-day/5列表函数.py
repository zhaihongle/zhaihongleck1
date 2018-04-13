list = []
def wangzhe(xx):
    list.append(xx)
while True :
    if len(list) == 5:
        xx = input('请输入英雄名字')
        print(list)
        break
    wangzhe(xx)
           
        
