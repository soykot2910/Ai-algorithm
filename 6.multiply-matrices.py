
def matrics(r,c):

    matrix=[]

    for i in range(r):
        a=[]
        for j in range(c):
            a.append(int(input()))
        matrix.append(a)
    return matrix

print("=========Enter first matrix======== ")
r1 = int(input("Enter the number of rows:"))
c1 = int(input("Enter the number of columns:"))
firstMatrix=matrics(r1,c1)

#matrix length will be matrix row
#matrix[0] means matrix column number
print("First matrix:")
for i in range(r1): #row ar jonno
    for j in range(c1): #column ar jonno
        print(firstMatrix[i][j],end=" ")
    print()

print("==========Enter second matrix========= ")
r2 = int(input("Enter the number of rows:"))
c2 = int(input("Enter the number of columns:"))
secondMatrix=matrics(r2,c2)

print("Second matrix:")
for i in range(r2):
    for j in range(c2):
        print(secondMatrix[i][j],end=" ")
    print()

# 0 means every value will be zero.
result=[[0 for x in range(r1)] for y in range(c2)]

print("Multiplication matrix:")
if r1==c2:
    for i in range(len(firstMatrix)):
        for j in range(len(secondMatrix[0])):
            for k in range(len(secondMatrix)):
                print(i,j,k)
                result[i][j] +=firstMatrix[i][k]*secondMatrix[k][j]

    for r in result:
        print(" ".join(map(str,r)))
else:
    print("Invalid input")
