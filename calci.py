print("Enter two numbers separated by a space")
x,y=[int(x) for x in input().split()]
print("Sum is :{0}".format(x+y))
print("Difference is :{0}".format(x-y))
print("Product is :{0}".format(x*y))
print("Quotient is :{0:.2f}".format(x/y))
