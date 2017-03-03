#Euler 5

#Problem:
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Author: Kshithij Iyer
#Date of creation: 13/1/2017

import time
#Recording start time of the program
start=time.time()
#logic to find  the number
for i in range(200000000,999999999):
    if i%1==0 and i%2==0 and i%3==0 and i%5==0 and i%7==0 and i%11==0 and i%13==0 and i%14==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0:
        print("The largest number that is divisible by all number between 1-20 is",i)
        break

print("Execution time of program is",time.time()-start)
