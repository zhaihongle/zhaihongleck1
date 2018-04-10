print('欢迎来到做菜系统'.center(20,"*"))
print('1：鸡蛋'.center(20,'*'))
print('2：土豆'.center(20,'*'))
print('3：茄子'.center(20,'*'))
print('4：黄瓜'.center(20,'*'))
list = []#[{热菜},{凉菜}，{汤}，{小菜}]
while True :
    fun_name = int(input('请选择蔬菜'))
    if fun_name == 1:
        name = input('请输入菜的名字')
