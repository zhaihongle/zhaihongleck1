while True:
	start = int(input("请输入一个数字:"))
	end = int(input("请输入一个数字:")) 
	sum = 0
	if start < end:
		for i in range(start,end+1):
			print(i)
			sum = sum+i
		print(sum)
		break
	else:
		print("输入有误")



# 如果输入有误，请重新输入，直到输入正确为止

"""
sum1 = 0
while start <= end:
	sum1= sum1+start
	start+=1

print(sum1)
"""
