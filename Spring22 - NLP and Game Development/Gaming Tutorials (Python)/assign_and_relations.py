# One can write more consise code by
# Using combined assingment and operations operator
# For example, a %= b return 5 when a is 11 and b is 71
# Always remember that "modulo" means wrapped around
# And floored returns int number of times b fits into a

a = 11
b = 71
a %= b
print(a) 

# Remember that readability counts (takes less time to understand the process going on)
# Also did you know that tabs can format output

print("a > b returns:\t\t", a > b)
print("While b < a returns:\t\t", a < b)

print(61 == 7 * (61 // 7) + 61 % 7)
print(61 // 7)
print(61 % 7)