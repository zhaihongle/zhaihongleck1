s_account = "xiaoyuan"
s_pwd = "123456"
count = 1 #用来记录输入有误的次数
while True:
	account = input("请输入账号")
	pwd = input("请输入密码")
	if account == s_account and pwd == s_pwd:
		choose_hero = int(input("0-ADC 1-肉 2-法师 3-刺客"))
		if choose_hero == 0:
			print("鲁班")
		elif choose_hero == 1:
			print("陈咬金")
		elif choose_hero == 2:
			print("妲己")
		elif choose_hero == 3:
			print("李白")
		
		break
	else:
		print("error%d次"%count)
		count+=1
		if count == 4:
			print("账号被封")
			break


