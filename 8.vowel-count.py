sen=input("Enter a sentence: ")
lowerCase=sen.lower()
vowelCount={} #dictonary
for vowel in "aeiou":
    count=lowerCase.count(vowel)#count method count korbe
    vowelCount[vowel]=count

print(vowelCount)
