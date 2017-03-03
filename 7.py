#Euler 7

#Problem:
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

#Author: Kshithij Iyer
#Date of creation: 15/1/2017

import time
#Recording start time of the program
start=time.time()
#Calculating the 10001st prime number
def primenumber(n):
    "A function to get the nth prime number"
    #counter for counting the prime numbers
    counter=5
    #A flag to identify the primes
    flag=1
    for i in range(13,105000):
        for j in range(2,i):
            if i%j==0:
                flag=0
                break;
            else:
                flag=1
        if flag==1:
            counter=counter+1
            #print(i," counter = ",counter)
        if counter==n:
            print("The",n,"st prime number is",i)
            return
#primenumber(6)
primenumber(10001)
print("Execution time of program is",time.time()-start)
