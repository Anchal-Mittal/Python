import calendar
def fun():
    print("check is 2008 is leap year or not ")
    if calendar.isleap(2008) :
        print("2008 is leap year")
    else:
        print("2008 is not leap year")
    
    print("no.of days between ",calendar.leapdays(2000,2016))    
fun();    

"""
isleap (year) :- This function checks if year mentioned in argument is leap or not.
leapdays (year1, year2) :- This function returns the number of leap days between the specified years in arguments.

"""
