def get_num (num):
    if num >= 1:
        return  num*get_num(num-1)
    else:
        return  1



#result = num*get_num(mum-1)   返回如下
#result= 5*result=4*get_num(4-1)
#result= 4*get_num(4-1)  

result = get_num(5)
print(result)
