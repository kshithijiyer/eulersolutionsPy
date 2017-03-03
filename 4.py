#Euler 4

#Problem:
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#Author: Kshithij Iyer
#Date of creation: 13/1/2017

import time
#Recording start time of the program
start=time.time()

def largestpalindrome():
    "A function to multiply the numbers and find the largest palindrome which is a multiple of two 3 digit numbers"
    #A varibale to store the product of the 3 digit and another to store the result for comparision
    result=1
    firstresult=0
    #999 becauese they are 3 digit numbers :p
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            result=i*j
            #Converting the number to string to check if they are palindrome or not.
            resultstring=str(result)
            reverseofresult=resultstring[::-1]
            if resultstring==reverseofresult:
                if i==995:
                    firstresult=result
                    break;
                if firstresult<result:
                    print("The largest palindorme made by the product of 2 number",i," and ",j," is ",result)
                    return
largestpalindrome()
print("Execution time of program is",time.time()-start)
