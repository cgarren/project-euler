import datetime
year = 1901
month = 1
day = 1
weekday = 1 #Tuesday
sunday_count = 0

thirtymonths = [4, 6, 9, 11]
thirtyonemonths = [1, 3, 5, 7, 8, 10, 12]

while year != 2001 or month != 1 or day != 1:
    #print(year, month, day, weekday)
    if weekday == 6 and day == 1:
        sunday_count += 1
        d = datetime.date(year, month, day)
        if d.weekday() == 6:
            sunday = True
        else:
            sunday = False
        #print(year, "Sunday number", sunday_count, "Day number", day, sunday)
    day += 1
    weekday += 1
    if weekday == 7:
        weekday = 0
    if month in thirtymonths:
        if day == 31:
            day = 1
            month += 1
    elif month in thirtyonemonths:
        if day == 32:
            if month == 12:
                day = 1
                month = 1
                year += 1
            else:
                day = 1
                month += 1
    elif month == 2:
        febdays = 28
        if year % 4 == 0:
            febdays = 29
            if year % 100 == 0:
                if year % 400 == 0:
                    febdays = 29
                else:
                    febdays = 28
        if day == febdays + 1:
            day = 1
            month += 1

    else:
        print("Error")
        break
print("Number of Sundays:", sunday_count)

#d = datetime.date(1901, 1, 1)
#print(d.weekday())
