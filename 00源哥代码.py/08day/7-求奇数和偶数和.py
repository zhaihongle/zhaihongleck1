i = 1
d_sum = 0 #定义偶数和
s_sum = 0 #定义奇数和
while i <=100:
	# 1 2 3 4 5 6 7....100
	if i%2 == 0: #偶数
		d_sum += i  #加起来的一定是偶数d_sum = d_sum + i
	else:
		s_sum += i  #加起来的一定是奇数s_sum = s_sum +i 

	i+=1

print("偶数和是%d"%d_sum)	
print("奇数和是%d"%s_sum)	








