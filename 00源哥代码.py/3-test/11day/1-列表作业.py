persons = ["laowang","laosong","laozhang"]
for i in persons:    
	print("我邀请%s共进晚餐"%i) 


#来不了
print("%s不能来了"%persons[0])



list = [4,5,6,7]

persons[0]= "laoliu"

for i  in persons:
	print("我邀请%s共进晚餐"%i)

#找到更大的餐桌,我要加人

persons.insert(0,"laozhao")
persons.insert(2,"laoli")
persons.append("laosun")
persons.append("aliang")

for i in persons:
	print("我邀请%s共进晚餐"%i)

"""
persons.remove("laosong")
persons.remove("laozhao")
persons.remove("laoli")
persons.remove("laosun")
print(persons)
"""

persons.sort()
print(persons)

length = len(persons)
print("长度是%d"%length)
