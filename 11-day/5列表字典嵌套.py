card = [{'名字':'尹天','年龄':'20岁','身高':'170厘米','特长':'臭不要脸'},{'名字':"豪哥","年龄":'20岁','身高':'175厘米'},{"名字":"崔建","年龄":"18岁","身高":"180厘米",'特长':'臭不要脸'}]
for i in card:
    print('')
    for x in i:
        print('%s:%s'%(x,i[x]))
