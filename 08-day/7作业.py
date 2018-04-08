x = 1
y = 0
while x <100:
    if x%2 == 0:
        y=y+x
    else:
        y=y-x
    x+=1
print(y)
print("*"*30)
x = 1
while x <= 5000:
    if x%5 == 0 and x%7 == 0:
        print(x)
    x+=1 
print("*"*30)     
import random
x = random.randint(1,100)
b = 0
while b <=10:
    z =int(input("请输入数字"))
    if z < x:
        print("你输入的数字偏小")
    elif z > x:
        print("你输入的数字偏大")
    elif z == x:
        print("恭喜你猜对了，好棒棒哦")
        break
    b+=1
