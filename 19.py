#Euler 19

#Problem:
#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

#Author: Kshithij Iyer
#Date of creation: 30/4/2017

import time
#Recording start time of the program
start=time.time()
#Importing the datetime package
import datetime
def Count_Sundays(From_year,To_year):
    "A function returns the count of Sundays"
    #A variable to keep the count of number of sundays
    number_of_sundays = 0
    for year in range(From_year,To_year+1):
        for month in range(1,13):
            # monday == 0, sunday == 6
            if datetime.datetime(year,month,1).weekday() == 6:
                number_of_sundays += 1
    return number_of_sundays

print("The number of sundays between 1901 to 2000 is",Count_Sundays(1901,2000));  
print("Execution time of program is",time.time()-start)
