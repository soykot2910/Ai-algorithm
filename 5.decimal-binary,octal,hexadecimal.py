decimal=int(input('Enter a decimal number: '))

print(decimal, "in binary",bin(decimal).replace("0b", "") )
print(decimal, "in Octal : ", oct(decimal).replace("0o", ""))
print(decimal, " in Hexadecimal : ", hex(decimal).replace("0x", ""))
