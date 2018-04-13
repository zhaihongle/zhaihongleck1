def jisuanqi(a,b,z):
    if z == '+':
        sum = x+y
        print(sum)
    elif z == '-':
        b = x-y
        print(b)
    elif z == '*':
        c = x*y
        print(c)
    elif z == '/':
        if y != 0:
            g = x/y
            print(g)
        else:
            print('cuowu')
while True:
    x = int(input('shuzi'))
    y = int(input('shuzi'))
    z = input ('+-*/')
    jisuanqi(x,y,z)
