
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# solution 1
total = 0
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		total += i 
print total

# solution 2 (Rob Zuber)
sq = sum([i for i in range(1000) if(i % 3 == 0 or i % 5 == 0)])
print sq

# solution 2+ (Rob Zuber)
sqs = sum(i for i in xrange(1000) if(i % 3 == 0 or i % 5 == 0))
print sqs
# This solution has a smaller footprint because xrange calls numbers into memory as they are needed instead of where range allocates 
# memory for all the objects up front. Another subtlety is that changing the [] brackets to () changes the array into a generator object
# which also consumes memory as it is needed.