
print("Enter Number:",end =" ")
n=int(input())
fiboPrev=0
fibo=1
print("Fibonacci sequence for {0} number:".format(n))

for i in range(n):
    print(fiboPrev,end=" ")
    fiboNext=fiboPrev+fibo
    fiboPrev=fibo
    fibo=fiboNext


