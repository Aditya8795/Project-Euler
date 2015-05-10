import math # for sqrt
# the trial factors need go no further than sqrt{n} because, if n is divisible by some number p,
# then n = p * q and if q were smaller than p, n would have earlier been detected as being divisible by q or a prime factor of q.

# This function checks if a number is prime, very small numbers (less than a million), trial division is the best way: divide by 2, 3, 5...
# and so on until the square root of the number. If you find a factor, the number is composite; otherwise, the number is prime.
# Used for problem #3
def isprime(x):
    if(x==2 or x==3 or x==5):
        return True
    if(x%2==0 or x%3==0):
        return False
    max_possible = int(math.sqrt(x))
    d, i = 5, 2 # i alternates as 2 then 4 then 2 then 4 and so on... while d takes on prime_sieve values - 5,7,11,13,17,19,23... 
    while(d<=max_possible):
        if(x%d==0):
            return False
        d = d + i
        i = 6 - i # causes the i alternation
    return True


# contains methods used for solving the problems @https://www.hackerrank.com/contests/projecteuler/challenges
class euler():

    def __init__(self):
        # Is used to keep track of how many times this "solver" object is called
        self.var = 0
        
    #   Project Euler #1: Multiples of 3 and 5
    # This function lists the sum of the multiples of 3 OR 5 which are LESS than N
    def problem1(self,list_of_N):
        N = list_of_N # list of N's
        n = len(N) # number of test cases
        for x in N:
            # we use x-1 as we don't count the multiples which are EQUAL to x
            # a, b, and c give us
            a = int((x-1)/3)
            b = int((x-1)/5)
            c = int((x-1)/15)
            # so we are going to print the SUM of the numbers below (NOT EQUAL to x)
            # such that the number is EITHER a multiple of 3 or 5
            # this is same as adding all multiples of 3 and 5 (which are less than x)
            # then subtracting all the multiples of 15 which are less than x once (as they repeat twice with both 3 and 5)
            ans = 3*a*(a+1) + 5*b*(b+1) - 15*c*(c+1)
            print ans//2
        self.var = self.var + 1 # the solver has been used once more

        ''' Project Euler #1: Multiples of 3 and 5

So initially I tried the brute force method for this problem
------------------------------
# Method - 1 BRUTE FORCE
for x in N:
    sum = 0
    for j in range(x):  # iterate through 0 to x and sum all the multiples of 3 or 5
        if(j%3==0 or j%5==0):
            sum=sum+j
    print sum
------------------------------
This didnt work for large numbers - RUNTIME ERROR

Another thing I learned while solving this problem is that
When you divide integers in python , the answer is converted
automatically to a float. Because it involves very large numbers,
when you convert back to integer, there will be a huge rounding error
and your answers will be wrong. thats why the following line failed for me,
        ans = 1.5*a*(a+1) + 2.5*b*(b+1) - 7.5*c*(c+1)
Thats why in the actual code above I stuck with whole numbers - 3,5 and 15
        '''

    #   Project Euler #2: Even Fibonacci numbers
    # This function lists the sum of the even-valued terms of the Fibonacci series whose values do not exceed the various N's
    def problem2(self,list_of_N):
        N = list_of_N # list of N's
        n = len(N) # number of test cases
        for x in N:
            ans = 0
            i = fib = 1 # fib(1)
            j = 2 # fib(2)
            while(fib<=x):
                if(fib%2 == 0):
                    ans = ans + fib
                fib = i + j # new fib --> fib(3), fib(4) ...
                # (i,j) becomes (2,3) (3,5) ... and so on from (1,2)
                i = j 
                j = fib
            # as the first 2 elements of the series isnt included in the summation, we add 2 (as 1 is not even) to the final sum
            print ans+2
        self.var = self.var + 1 # the solver has been used once more
        
        ''' Project Euler #2: Even Fibonacci numbers

So initially I tried the following method
------------------------------
# Method - 1 BRUTE FORCE
for x in N:
    ans = 0
    i = 1
    while(fib(i)<=x):
        temp = fib(i) # so that we dont need to call fib twice
        if(temp%2 == 0):
            ans = ans + temp
        i = i + 1
    print ans
------------------------------
This didnt work for large numbers - Terminated due to timeout
Here fib was the following function ->

def fib(n):
    # n'th fibbonaci number
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    return fib(n-1) + fib(n-2)

So, yeah this wasnt clever as they called this recursive function a whole lot of times...
        '''

    #   Project Euler #3: Largest prime factor
    # This function prints the largest prime factor of the N's
    def problem3(self,list_of_N):
        N = list_of_N # list of N's
        n = len(N) # number of test cases
        for x in N:
            latest_prime = 0
            for i in range(x,1,-1): # consider all numbers from x to 2
                if(x%i==0): # check if its a factor of x
                    if(isprime(i)): # check if its prime
                        latest_prime = i
                        break # the first answer we find is the answer
            print latest_prime

                
''' PROBLEM UNSOLVED 
Method - 1 BRUTE FORCE 

I am facing Runtime error

'''


# =================================================================================================== END OF CLASS euler

# Testing the solutions with Sample Output from HackerRank

solve1 = euler() # make an object of euler class
print "Problem 1 solution for 10,100 is =>"
solve1.problem1([10,100]) # I get output  23, 2318

solve2 = euler() # make an object of euler class
print "Problem 2 solution for 10,100 is =>"
solve2.problem2([10,100]) # I get output  10, 44

solve3 = euler() # make an object of euler class
print "Problem 3 solution for 10,17 is =>"
solve3.problem3([10,17]) # I get output  5, 17
