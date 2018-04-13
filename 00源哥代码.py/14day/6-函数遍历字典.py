list=[{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]


for i in list:
	#print(i)
	#i是字典
	for k,v in i.items():
		#k = beijing
		#v = {"mianji":1290}
		print(k)
		print(v)
		for j,l in v.items():
			print(k,j,l)
