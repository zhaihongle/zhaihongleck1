# elif 执行到这一步就不往下执行了
# if 会一直执行到最后，，
# 优化后节省了运行空间

x = float(input("请输入数字"))
y = float(input("请输入数字"))
fuhao = input("请输入+-*/")
if fuhao == '+':
    print(x+y)
elif fuhao == '-':
    print(x-y)

