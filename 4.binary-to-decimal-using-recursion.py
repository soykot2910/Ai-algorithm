def  binToDec(num):
    if num ==1 or num == 0:
        return num

    length=len(str(num))
    firstDigit=num//pow(10,length-1)
    return (pow(2,length-1)*firstDigit)+binToDec(num%pow(10,length-1))

binary=int(input('Enter a binary number: '))
decimal=binToDec(binary)

print('Deccimal of {0} is {1}'.format(binary,decimal))

