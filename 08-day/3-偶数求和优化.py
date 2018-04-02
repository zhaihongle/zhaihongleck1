i = 1 
d_sum = 0 
f_sum = 0
while i <= 100:
    if i%2==0:
        d_sum+=i
    else:
        f_sum+=i
    i+=1
print("偶数和是%d"%d_sum)
print("基数和是%d"%f_sum)
