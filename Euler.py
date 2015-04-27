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

        '''
SO initially I tried the brute force method for this problem
------------------------------
# Method - 1 BRUTE FORCE
n = int(raw_input()) # number of test cases
N = [] # list of N's 
for i in range(n):
    N.append(int(raw_input()))
    
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


solve1 = euler() # make an object of euler class
print "Problem 1 solution for 10,100 is =>"
solve1.problem1([10,100]) # I get output  23, 2318

