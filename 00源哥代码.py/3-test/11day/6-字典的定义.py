id_card = {"name":"张三","age":12,"sex":"男","group":"汉"}

print(id_card)
#增加
id_card["address"] = "北京市"
id_card["merry"] = "单身狗"
id_card.setdefault("age",14)
id_card.setdefault("height",175)
print(id_card)
#删除
id_card.pop("merry")
id_card.popitem() #随机删除一个键值对
#id_card.clear()

#del id_card["age"]
#修改

id_card["name"] = "李四"

#查
print(id_card["name"])
#print(id_card["merry"])没有这个键会报错
print(id_card.get("merry"))

#合并
id_card2 = {"name":"王五","weight":230}
id_card.update(id_card2)
print(id_card)

#所有的键
print(id_card.keys())
#所有的值
print(id_card.values())
#键值对形式返回
print(id_card.items())
