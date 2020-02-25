def calc_hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf

num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
print("The H.C.F of {} and {} is {}".format(num1,num2,calc_hcf(num1,num2)))