
def matrics(r,c):

    matrix=[]

    for i in range(r):
        a=[]
        for j in range(c):
            a.append(int(input()))
        matrix.append(a)
    return matrix

r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
firstMatrix=matrics(r,c)

print("matrix:")
for i in range(r):
    for j in range(c):
        print(firstMatrix[i][j],end=" ")
    print()

result=[[ 0 for x in range(r)] for y in range(c)]

for i in range(len(firstMatrix)): #row length
        for j in range(len(firstMatrix[0])): #firstMatrix row length
            result[j][i]=firstMatrix[i][j]

print("Transpose matrix:")
for r in result:
    print(r)
