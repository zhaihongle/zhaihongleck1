#服务器存的账号和密码
s_acc = "123456"
s_pwd = "123456"
print("TIMI")
choose_login = int(input("请选择登录方式　1=qq 2=微信 3=账号"))


if choose_login == 1:
	print("qq登录成功")
	choose_hero = int(input("请选择英雄　1=战士2=法师3=刺客4=射手5=辅助"))

	if choose_hero == 1:
		print("死亡骑士")
	elif choose_hero == 2:
		print("愿意为主人服务")
	elif choose_hero == 3:
		print("大河之剑天上来")
	elif choose_hero == 4:
		print("智商二百五")
	elif choose_hero == 5:
		print("骑鱼的男人")


elif choose_login == 2:
	print("微信登录成功")
elif choose_login ==3:
	account = input("请输入账号")
	pwd = input("请输入密码")
	if account == s_acc and pwd == s_pwd:
		print("账号登录成功")
	else:
		print("登录失败")	

