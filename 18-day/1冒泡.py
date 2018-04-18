list = [1,3,6,8,3,9,5,5,7,8,6,4]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print(list)
