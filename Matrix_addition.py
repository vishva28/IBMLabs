r=int(input("Enter number of rows: "))
c=int(input("Enter number of columns: "))
print("Enter first {}*{} matrix".format(r,c))
mat1=[]
for i in range(r):
    a=[int(a) for a in input().split()]
    mat1.append(a)
print("Enter second {}*{} matrix".format(r,c))
mat2=[]
for i in range(r):
    a=[int(a) for a in input().split()]
    mat2.append(a)
resultant_matrix=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(mat1[i][j] + mat2[i][j])
    resultant_matrix.append(a)
print("The resultant matrix after addition is ")
for i in range(r):
    for j in range(c):
        print(resultant_matrix[i][j],end=" ")
    print()
