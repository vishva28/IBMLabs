def calc_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
print("The L.C.M  of {} and {} is {}".format(num1,num2,calc_lcm(num1, num2)))
