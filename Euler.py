# We define useful FFUNCTIONS BELOW

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



# ========================================================================== START OF CLASS euler


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
			print(ans//2)
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
			print(ans+2)
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

		So, yeah this wasn't that clever as they called this recursive function a whole lot of times...
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
				print(latest_prime)

				
		'''  PROBLEM UNSOLVED 
		Method - 1 BRUTE FORCE 

		I am facing Runtime error

		'''

	#   Project Euler #28: Number spiral diagonals
	# This function prints the sum of the diagonal elements for a N*N spiral.
	# The spiral is drawn starting with 1 then to the right clockwise.
	def problem28(self,list_of_N):
		N = list_of_N # list of N's
		n = len(N) # number of test cases
		for i in N:
			r = i//2
			print(round(4*r + (2.66666666667)*r*(r+1)*(2*r+1) - 8*r*(r+1) + 10*r*(r+1))+1)

		self.var = self.var + 1 # the solver has been used once more
		
		''' Project Euler #28: Number spiral diagonals

		So I saw how the 1*1 spiral has only 1. Then the 3*3 spiral additionally
		has 3, 5, 7, 9. The 5*5 spiral has additionally 13, 17, 21, 25.
 
		I noticed how these form a set of quadruplets -> {3, 5, 7, 9}, {13, 17, 21, 25},
		{31, 37, 43, 49} ...

		if we number the above sequence we can note the required "sum of diagonals" for N*N 
		is (sum of all the terms of this sequence up to the rth term) plus 1.
		N = 3, r should be 1. N = 5, r should be 2, and so you should see r is N//2 
		(integer division or floor division in python).

		OK now we can just find a general expression for this sequence and then apply summation.
		but note we don't care about the individual elements in the quadruplets, we care about its sum.

		The above logic will equally apply if we talk about the sum of all the terms of this sequence up to the rth term,
		{3 + 5 + 7 + 9}, {13 + 17 + 21 + 25}, {31 + 37 + 43 + 49} ...

		= {(1+1*2) + (1+2*2) + (1+3*2) + (1+4*2)}, 
		  {(9+1*4) + (9+2*4) + (9+3*4) + (9+4*4)},  Note 9 is the last term of the previous quadruplet.
		  {(25+1*6) + (25+2*6) + (25+3*6) + (25+4*6)} ...

		  the sum in each term of the sequence can be written as,

		= {4*(1) + 2*(1+2+3+4)}, 
		  {4*(9) + 4*(1+2+3+4)},
		  {4*(25) + 6*(1+2+3+4)} ... 

		  where the terms 1, 9, 25, 49 follow the following sequence
		  1, (1+4*2), (1+4*2+4*4), (1+4*2+4*4+4*6), ...

		  the ith term will be 1 + 4(2 + 4 + 6 + ... 2(i-1)) = 1 + 8 * ((i-1)*i)/2
		   = 1 + 4*(i-1)*i

		   using this we can write the ith term of the main sequence as,

		= {4*(1) + 2*(10)}, 
		  {4*(9) + 4*(10)},
		  {4*(25) + 6*(10)} ... 
		  {4*(1 + 4*(i-1)*i) + 2*i*10} ...

		  Coming to the solution for N*N spiral we need to sum this above sequence for r terms
		  as discussed above,

		  Sigma {4 + 16*(i*i) - 16*i + 2*i*10}
		  = 4*r + (16/6)*r(r+1)(2r+1) - 8*r(r+1) + 10*r(r+1)

		  Thus I solved this problem - http://i.imgur.com/FPYqFvi.png
		'''

# ========================================================================== END OF CLASS euler

# Testing the solutions with Sample Output from HackerRank

solve1 = euler() # make an object of euler class
print("Problem 1 solution for 10,100 is =>")
solve1.problem1([10,100]) # I get output  23, 2318

solve2 = euler() # make an object of euler class
print("Problem 2 solution for 10,100 is =>")
solve2.problem2([10,100]) # I get output  10, 44

solve3 = euler() # make an object of euler class
print("Problem 3 solution for 10,17 is =>")
solve3.problem3([10,17]) # I get output  5, 17

solve28 = euler() # make an object of euler class
print("Problem 28 solution for 3, 5, 7 is =>")
solve28.problem28([3,5,7]) # I get output  5, 17
