print("作业一：")
for i in range(1,5000+1):
    if i%5==0 and i%7==0:
        print(i)
        
print('作业二')
import random 
x = random.randint(1,100)
for i in range (11):
    a =int(input('请输入数字'))
    if a< x:
        print('你输入的数字偏小')
    elif a >x :
        print('你输入的数字偏大')
    elif a == x:
        print('恭喜你猜对啦')
        break
print('作业三')
s_account = '猪'
s_pwd =int("123456")
a = input('请输入名字')
b = int(input('请输入密码'))
if a == s_account and b == s_pwd:
    print('欢迎来到猪世界')
elif a != s_account:
    print('名字输入错误')
elif b != s_pwd :
    print('密码输入错误')

print('祖业四')
for i in range(5):
    for x in range (1,i+1):
        print('*',end="")
    print('')  

print("作业五")
