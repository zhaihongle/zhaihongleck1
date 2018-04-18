list = [13,6,10,21,30,50,4,89,2]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print(list)
key = 4
center = int(len(list)/2)
while True:
    if key > list[center]:
        center+=1
    elif key < list[center]:
        center-=1
    elif key == list[center]:
        print('4在%d位'%center)
        break
