def jisuanqi(a,b,z):
    if z == '+':
        i = x+y
        #return i
    elif z == '-':
        i = x-y
        #return i
    elif z == '*':
        i = x*y
        #return i
    elif z == '/':
        if y != 0:
            i = x/y
            #return i
        else:
            print('cuowu')
    return i
    
while True:
    x = int(input('shuzi'))
    y = int(input('shuzi'))
    z = input ('+-*/')
    i = jisuanqi(x,y,z)
    print(i)
