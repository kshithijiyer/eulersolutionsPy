#Euler 6

#Problem:
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Author: Kshithij Iyer
#Date of creation: 15/1/2017

import time
#Recording start time of the program
start=time.time()
#Variables to store the square of sum and sum of square
square_of_sum,sum_of_square=0,0
#Logic to find out the square of sum and sum of square
for i in range(1,101):

    square_of_sum=square_of_sum+i

    sum_of_square=sum_of_square+(i**2)
    
square_of_sum=square_of_sum**2
difference=square_of_sum-sum_of_square

print("The difference between the sum of the squares of the first 100 natural numbers and square of sum is",difference)
print("Execution time of program is",time.time()-start)
