list = [2,3,4,5,6,7,8,13,25,47,59]
num = int(input("数字"))
center = int(len(list)/2)
if num in list:
    while True:
        if num > list[center]:
            center+=1
        elif num < list[center]:
            center-=1
        elif num == list[center]:
            print('数字%s的索引是%s'%(num,center))
            break
else:
    print('没有')
            
