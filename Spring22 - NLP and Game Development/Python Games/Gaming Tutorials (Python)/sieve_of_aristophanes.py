# The sieve of aristophanes is an algorithm for find every prime number within a range of numbers
# And it is a relatively efficent algorithm
# Starting with 2 we see if a number is prime by checking if it is divisible by any of the prime numbers that come before it
# If it does not, the when add it to the prime number list

from pprint import pprint

prime_numbers = [2]

n = int(input("""The sieve of Aristophanes is an algorithm designed to find the first n prime numbers.
Please enter the number of primes you wish to find: """))

while n > 100 or n < 1:
	n = int(input("""Please enter a number between 1 - 99: """))
	

for i in range(3, 100000, 2):
	# If we have range prime numbers, we can exit the loop
	if len(prime_numbers) == n:
		break

	# Starting assumption
	is_prime = True

	for prime in prime_numbers:
		if i % prime == 0:
			is_prime = False
			break
	if is_prime:
		prime_numbers.append(i)

			
		
pprint(prime_numbers)
