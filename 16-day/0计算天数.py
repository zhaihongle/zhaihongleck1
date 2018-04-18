def count_day(date):
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:])
    galg = False #平年  
    if year%400 == 0 or (year%4==0 and year%100!=0):
        galg = True #闰年
    big_month = [1,3,5,7,8,10,12]
    small_month = [4,6,9,11]
    all_day = 0
    for i in range(1,month):
        if month in big_month:
            all_day+=31
        elif month in small_month:
            all_day+=30
        elif month == 2 and galg == True:
            all_day+=29
        elif month == 2:
            all_day+=28
    all_day+=day
    print('天数是%d'%all_day)
date = input('nianyuri')
count_day(date)
