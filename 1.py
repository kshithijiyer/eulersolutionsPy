#Euler 1

#Problem:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Author: Kshithij Iyer
#Date of creation: 12/1/2017

import time
#Recording start time of the program
start=time.time()
#A variable to store the sum 
result=0

#calculating the sum for all the numbers below 1000
for i in range(1,1000):
    #Checking the the condition 
    if i%3==0 or i%5==0:
        result=result+i
        #print(result)

print("Sum of all numbers that are multiples of 3 or 5 below 1000 is",result)
print("Execution time of program is",time.time()-start)
