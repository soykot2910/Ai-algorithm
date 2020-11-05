print("Enter two number lower and upper range:")
lower=int(input())
upper=int(input())

for num in range(lower,upper+1):
    total=0
    temp=num
    while temp>0:
        singleDigit=temp%10
        total +=singleDigit**3 #exponential
        temp //=10 #it's give only integer value
    if num==total:
          print(num)


