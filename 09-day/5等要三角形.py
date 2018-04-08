i = 1
while i <= 5:
    j = 5
    while j >= i:
        print(" ",end="")
        j-=1
    k = 1
    while k <= i:
        print("* ",end="")
        k+=1
    print("")
    i+=1
