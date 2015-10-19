# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


val = 600851475143
# val = 60000000
n = 2
factors = []
pfactors = []
while n < val**.5:
	if val % n == 0:
		'''n is a factor of 'val' the target value'''
		factors.append(n)
		'''Check if 'n' is a prime number and add it to list'''
		prime = 1
		for i in range(2, n):
			if n % i == 0:
				'''n is not prime'''
				prime = 0
				break
		if prime:
			pfactors.append(n)
	n = n + 1
print factors
print max(pfactors)