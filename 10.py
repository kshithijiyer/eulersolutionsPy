#Euler 10

#Problem:
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

#Author: Kshithij Iyer
#Date of creation: 15/1/2017

import time
#Recording start time of the program
start=time.time()
def sum_of_prime_numbers(limit):
    "A function to get the sum prime numbers till the limit"
    #Variable to store the sum of prime numbers
    sum_of_prime=0
    #Sieve of Eratosthenes algorithm
    sieve=[True]*limit
    for i in range(2,limit):
        if sieve[i]:
            sum_of_prime=sum_of_prime+i
            for j in range(i*i,limit,i):
                sieve[j]=False
            #print(i,"",sum_of_prime)
    print("The sum of all the prime numbers below",limit,"is",sum_of_prime)
    return
#sum_of_prime_numbers(10)
sum_of_prime_numbers(2000001)
print("Execution time of program is",time.time()-start)

#Note:
#I did give the conventioanl method a try but it didn't work well and was taking some 13 minutes to get the results.

#Algorithm for reference
#Input: an integer n > 1

#Let A be an array of Boolean values, indexed by integers 2 to n, initially all set to true.
 
#for i = 2, 3, 4, ..., not exceeding √n:
#if A[i] is true:
#for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n :
#A[j] := false
 
#Output: all i such that A[i] is true.
