print('1-石头')
print('2-剪刀')
print('3-布')
import random 
i = int(input("请输入次数"))
j = 1
while j <= i :
    computer = random.randint(1,3)
    player = int(input('请输入1,2,3'))
    if (player ==1 and computer ==2) or (player ==2 and computer ==3) or (player ==3 and computer ==1):
        print('你赢了') 
    elif player==computer:
        print('再来一局')
    else:
        print('你输了')
    j+=1
