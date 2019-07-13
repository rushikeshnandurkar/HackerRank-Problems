#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    list_of_30 = [4,6,9,11]
    list_of_31 = [1,3,5,7,8,10,12]

    next_year = year

    if month in list_of_31:
        if day == 31:
            next_day = 1
            next_month = (month + 1)%12
            if next_month == 1:
                next_year += 1
        else:
            next_day = day + 1
    elif month in list_of_30:
        if day == 30:
            next_day = 1
            next_month = (month + 1) % 12
        else:
            next_day = day + 1
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if day == 29:
                next_day = 1
                next_month = month + 1
            else:
                next_day = day + 1
        else:
            if day == 28:
                next_day = 1
                next_month = month + 1
            else:
                next_day = day + 1

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(30,6,2015)