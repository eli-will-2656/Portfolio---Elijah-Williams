# Conditional Expressions
# In C++, there is something called the ternary operator "?" which allows one to return a value based on a condition
# Although there is no such ternary operator in python, there is what is called a "conditional expression"
# Expression = Something that returns a value
# Statement = Does not have to return a value

import sympy

first_10_primes = list(sympy(0,10))

for i in range(5):
	print(i, end=" ")
	print("Even" if i % 2 == 0 else "Odd")
	print("Prime" if i in first_10_primes else "Not Prime")