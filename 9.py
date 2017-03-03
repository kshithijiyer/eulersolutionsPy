#Euler 9

#Problem:
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#Author: Kshithij Iyer
#Date of creation: 

import time
#Recording start time of the program
start=time.time()
#Logic to check generate numbers for a,b,c
for a in range(200,500):
    for b in range(225,500):
        for c in range(250,500):
            #checking the first condition
            if a+b+c==1000:
                #Checking the second condition
                if a<b<c:
                    #Checking the third condition
                    if a**2+b**2==c**2:
                        print("The product of abc which are",a,b,c,"respectively is",(a*b*c))
print("Execution time of program is",time.time()-start)
