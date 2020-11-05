# recursion is a process where a function calls itself
# directly of indirectly
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

print("Enter Number:",end =" ")
number=int(input())

for i in range(number):
    print(fibo(i),end=" ")
