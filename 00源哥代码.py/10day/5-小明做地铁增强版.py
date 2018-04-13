all_sum = 0#总钱
for i in range(1,13):
	sum = 0 #每月花的多少钱
	money = 0#单次钱数
	distance = 0
	if i == 1 or i == 12:
		distance = 32 #距离
	elif i == 2  or i == 11:
		distance = 18
	elif i == 3  or i == 10:
		distance = 7
	elif i == 4  or i == 9:
		distance = 80
	elif i == 5  or i == 8:
		distance = 34
	elif i == 6  or i == 7:
		distance = 70
	for  j  in range(0,60):
		if  distance <= 6:
			money = 3
		elif distance > 6 and distance <=12:
			money = 4
		elif distance > 12 and distance <=22:
			money = 5
		elif distance > 22 and distance <=32:
			money = 6
		elif distance > 32: 
			if (distance - 32)%20 == 0:
				money = 6 + (distance-32)/20
			else:
				money = 6+ int((distance-32)/20) + 1

		if sum >= 100 and sum < 150: 
			money = money * 0.8
		elif sum>=150 and sum < 400:
			money = money * 0.5
		
		sum = sum+money
	print("%d月花了%0.2f"%(i,sum))

	all_sum = all_sum + sum
print("钱是%0.2f"%all_sum)












