def file():
    for i in range(10):
        for j in range(i+1):
            print('%d*%d=%d'%(i,j,i*j),end=" ")
        print('')

file()
