list= [{'beijing':{'renkou' :' 10000','roujou' : '200000'}},{'shanghai':{'renkou' :'11111 ', 'mianji' : '22222'  }}]
for temp in list:
    #temp = 大字典
    for address,s_num in temp.items():
       #address= 大组点的建
            for name  in s_num:
                print('%s:%s:%s'%(address,name,s_num[name]))
