
import calendar

print ("The calender of year 2012 is : ")
print (calendar.calendar(2012,2,1,6))# year=2012,width=2,no_of_lines_per_weeks =1,column_separations=6

#using firstweekday() to print starting day number
print ("The starting day number in calendar is : ",end="")
print (calendar.firstweekday())

"""
Operations on calendar : 
1. calendar(year, w, l, c) :- This function displays the year, width of characters, no. of lines per week and column separations.
2. firstweekday() :- This function returns the first week day number. By default 0 (Monday).

"""
