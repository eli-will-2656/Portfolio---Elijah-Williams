a,b,c = 2,4,8

# Here we see the precedence of multiplication operator over addition
print("\nDefault Order:\t", a, '*', b, "+", c, "=", a*b+c, sep="")
print("\nForced Order:\t", a, '*(', b, "+", c, ")=", a*(b+c), sep="")
print()
# Here we see the precedence of exponentiation over multiplcation
print("\nDefault Order:\t", a, '**', b, "*", c, "=", a**b*c, sep="")
print("\nForced Order:\t", a, '**(', b, "*", c, ")=", a**(b*c), sep="")

