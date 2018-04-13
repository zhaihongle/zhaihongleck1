cards = [{"name":"尹天","age":20},{"name":"豪哥","age":20},{"name":"崔健","age":18}]

for i in cards:
	for k,v in i.items():
		print("%s:%s"%(k,v))


d = {}
d["name"] = "xiaoyuan"
cards.append(d)
print(cards)	
