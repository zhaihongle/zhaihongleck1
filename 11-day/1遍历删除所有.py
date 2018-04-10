"""
list = [1,2,3,4,5,5]
for i in range(len(list)):
    list.pop(0)
print(list)

list1 = [1,2,3,4,5,6] 
for x in range (len(list)-1,-1,-1):
    list.remove(x)
print(list1)
"""

list2 = [1,2,3,3,4,5,6]
new_list = list2 [ : ]
for j in new_list: 
    list2.remove(j)
print(list2)
