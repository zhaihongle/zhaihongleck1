games = [["传奇","贪玩蓝月"],["QQ飞车","QQ炫舞"],["天天酷跑","天天炫斗"],["王者荣耀","绝地求生"]]

for i in games:
	for j in i:
		print("这个游戏是%s"%j)


i = 0

while i < len(games):# 0 1 2 3
	#print(games[i])
	j  = 0 
	while j < len(games[i]):#  0 ,1 
		print("这while遍历的%s"%games[i][j])
		j+=1

	i+=1	
		
