import cmath
a=int(input("Enter the coefficient of x**2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the constant: "))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("The solutions are {} and {}".format(sol1,sol2))