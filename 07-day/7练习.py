h =int(input('请输入身高'))
s =int( input('请输入身价'))
y =int( input('请输入颜值分'))
if h >=180 and s >= 1000000 and y > 99:
    print('你是高富帅')
elif s > 99:
    print('帅')
elif h < 160 and s < 100 and y < 60:
    print('你是矮挫')
