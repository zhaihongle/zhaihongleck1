#坑一
"""
list = [1,2,3,4,5,6,7]
for i in list:
	list.remove(i)

print(list)
"""

"""
list = [1,2,3,4,5,6,7]
for i in range(len(list)):
	list.pop(i)
"""

#第一种　倒着删
#第二种　复制一个新列表　操作原始列表


"""
list = [1,2,3,4,5,6,7]

for i in range(len(list)-1,-1,-1):
	list.pop(i)

print(list)
"""

list = [1,2,3,4,5,6,7]

new_list = list[:]
for i in new_list:
	list.remove(i)


print(list)
	 


