def s_math():
    for i in range(100,201):
        flag = 0
        for j in range (2,i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            print(i)

s_math()
