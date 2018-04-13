#5排6列

test = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]

test[0][1]#第一排第二列的同学

for i  in test:
	print("第%s排"%str(i))
	for j  in i:
		print(j)

i = 0

while i < len(test): #i =  0,1,2,3,4　排数
	test[i]
	j = 0
	while j < len(test[i]):# j = 0,1,2,3,4,5 列数
	#	print(test[0][0])	
		print(test[i][j],end='')

		j+=1
	print("")	

	i+=1
