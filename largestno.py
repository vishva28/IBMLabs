print("Enter three numbers separated by a space")
x,y,z=[float(x) for x in input().split()]
print("The greatest number among the three is : ",end="")
if x>=y and x>=z:
    print(x)
elif y>=x and y>=z:
    print(y)
else:
    print(z)