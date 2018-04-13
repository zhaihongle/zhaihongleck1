t = ("laowang","laosong","laoliu")#元组
s = input("请输入一个名字")

if s in list(t):
	print("laowangzai")
else:
	print("buzai")


if s not in t:
	print("buzai")
else:
	print("zai")



