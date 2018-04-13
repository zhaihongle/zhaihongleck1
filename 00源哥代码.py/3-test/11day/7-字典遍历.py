dict = {"name":"小明","age":40,"性别":"男"}

for i in dict:
	print(i)
	print(dict.get(i))


for i in dict.keys():
	print(i)
	print(dict.get(i))#dict[i]

for i in dict.values():
	print(i)


for k,v in dict.items():
	print("%s的值是%s"%(k,v))

