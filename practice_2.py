#Problem 1--->

text='pHitrOn.iO presents "Python COuRSe".'
string=''
for char in text:
    if char>='a' and char<='z':
        string+=chr(ord(char)-32)
    elif char>='A' and char<='Z':
        string+=chr(ord(char)+32)
    else:
        string+=char
print(string)

#problem 2

number=int(input("Enter any number: "))
for i in range(1,number+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    
#problem 3

