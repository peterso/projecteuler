# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10
# terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

def fib(numOfTerms):
	fib = 0
	evensum = 0
	i = 0

	m = 1
	n = 2
	seq = [m,n]
	while fib < numOfTerms:
		if n % 2 == 0:
			evensum = evensum + n
		fib = m + n
		m = n
		n = fib
		seq.append(fib)
		i = i + 1

	print evensum
	print seq


# Solution #2
def fib2(numOfTerms):
	a, b = 1, 1
	sequence = [a]
	for i in range(numOfTerms-1):
		a,b = b, a+b
		sequence.append(b)
	print sequence
	print sum(i for i in sequence if i % 2 == 0)

#straight jacket, for mission critical code.