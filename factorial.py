print("Enter a number : ",end="")
n=int(input())
fact=1
if n<0:
    print("Does not exists")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("The Factorial of {0} is {1}".format(n,fact))