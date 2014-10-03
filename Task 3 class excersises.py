#Aaron Bentley
#3/10/2014
#Gross pay excersise

hours_worked = int(input("Please enter your hours worked: "))
hours_pay = int(input("Please enter your hourly rate of pay: "))
if 40 < hours_worked < 60:
    Standard_wage = 40*hours_pay
    extra_pay = (hours_pay*1.5)*(hours_worked-40)
    total = Standard_wage+extra_pay
    print("your wage is £{0}".format (total))   
else:
    print("insufficient hours")
    
