xx = input('请输入位置 adc rou fa cike')
if xx == "adc":
    print('后裔 黄总 虞姬')
elif xx == "rou":
    print("亚瑟 chengyaojin")
elif xx == 'fa':
    print("zhiajun danji")
elif xx == ('cike'):
    print('lanawang  keke')

print('*'*30)
year=int( input('nianfen'))
if (year%400==0) or (year%4==0 and year%100!=0):
    print('ruinian')
else:
    print('pingnian')
print('*'*30)
h = float(input("请输入身高"))
w = float(input("请输入体重公斤"))
b = w/(h**2)
if b < 18.5 :
    print("guoqing")
elif b >= 18.5 and b <25:
    print ("zc")
elif b >= 25 and b <28:
    print('feip')
