
```
OUTPUT "enter date in dd/mm/yy"
var  ← day
var  ← month
var  ← year

IF month ← 12 THEN
	month ← "December"
ELSE month ← 11 THEN
	month ← "November"
ELSE month ← 10 THEN
	month ← "October"
ELSE month ← 9 THEN
	month ← "September"
ELSE month ← 8 THEN
	month ← "August"
ELSE month ← 7 THEN
	month ← "july"
ELSE month ← 6 THEN
	month ← "june"
ELSE month ← 5 THEN
	month ← "May"
ELSE month ← 4 THEN
	month ← "April"
ELSE month ← 3 THEN
	month ← "March"
ELSE month ← 2 THEN
	month ← "febuary"
ELSE month ← 1 THEN
	month ← "January"
ENDIF:
	OUTPUT "NOT A MONTH"

IF 31 <= year < 100 THEN
	year_full ← 19
ELSE 00 <= year < 31
	year_full ← 20
ENDIF

IF day = 1 THEN
	OUTPUT "{0}st {1} {2}{3}".FORMAT (day,month,year,year_full)
ELSE day = 21 THEN
	OUTPUT "{0}st {1} {2}{3}".FORMAT (day,month,year,year_full)
ELSE day = 31 THEN
	OUTPUT "{0}st {1} {2}{3}".FORMAT (day,month,year,year_full)
ELSE day = 2 THEN
	OUTPUT "{0}nd {1} {2}{3}".FORMAT (day,month,year,year_full)
ELSE day = 22 THEN
	OUTPUT "{0}nd {1} {2}{3}".FORMAT (day,month,year,year_full)
ELSE day = 3 THEN
	OUTPUT "{0}rd {1} {2}{3}".FORMAT (day,month,year,year_full)
ELSE day = 23 THEN
	OUTPUT "{0}rd {1} {2}{3}".FORMAT (day,month,year,year_full)
ENDIF:
	OUTPUT "{0}TH {1} {2}{3}".FORMAT (day,month,year,year_full)



	 
```