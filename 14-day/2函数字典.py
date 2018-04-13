#yyxx = [{beijing{renkou : xxx,roujou :xxxx}},{shanghai:{renkou : , mianji :  }}]
#beijing:renkou :xxx
#beijing :mianji :xxx
#beijing :mianji :xxx
#shanghai :  mianji :xx
#shanghai :  mianji :xx
list= [{'beijing':{'renkou' :' 10000','roujou' : '200000'}},{'shanghai':{'renkou' :'11111 ', 'mianji' : '22222'  }}]
for temp in list:
    #temp = 大字典
    for address , s_num in temp.items():
       #address= 大组点的建
           # print('%s:%s'%(address,temp[address]))
            for name , s_name in s_num.items():
                print('%s:%s:%s'%(address,name,s_name))


















