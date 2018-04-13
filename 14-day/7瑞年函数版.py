def s_year (year):
    if year%400 ==0 or (year%4==0 and year%100!=0 ):
        print('瑞年')
    else:
        print('平年')
while True:
    year = int(input('年份'))
    s_year(year)
