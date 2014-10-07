print("enter date in dd/mm/yy")
day = int(input("Day: "))
month = int(input("month: "))
year = int(input("Year: "))

if month == 12:
    month = ("December")
elif month == 11:
    month = ("November")
elif month == 10:
    month = ("October")
elif month == 9:
    month = ("September")
elif month == 8:
    month = ("August")
elif month == 7:
    month = ("July")
elif month == 6:
    month = ("June")
elif month == 5:
    month = ("May")
elif month == 4:
    month = ("April")
elif month == 3:
    month = ("March")
elif month == 2:
    month = ("February")
elif month == 1:
    month = ("January")
else:
    print("{0} This is not a month".format (month))

if 31 <= year < 100:
    year_full = 19
elif 0 <= year < 31:
    year_full = 20

if day == 1:
    print("{0}st {1} {2}{3}".format (day,month,year_full,year))
elif day == 21:
    print("{0}st {1} {2}{3}".format (day,month,year_full,year))
elif day == 31:
    print("{0}st {1} {2}{3}".format (day,month,year_full,year))
elif day == 2:
    print("{0}nd {1} {2}{3}".format (day,month,year_full,year))
elif day == 22:
    print("{0}nd {1} {2}{3}".format (day,month,year_full,year))
elif day == 3:
    print("{0}rd {1} {2}{3}".format (day,month,year_full,year))
elif day == 23:
    print("{0}rd {1} {2}{3}".format (day,month,year_full,year))





    
    
