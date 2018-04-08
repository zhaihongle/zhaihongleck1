
while True:
    x = int(input("请输入数字"))
    xx = int(input("请输入数字\n大于上一次数字"))
    sum = 0
    if x < xx:
        for i in range(x,xx+1):
            print(i)
            sum=sum+i

        break    
print(sum) 
