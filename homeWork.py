for i in range(13,40,2):
    print(i)
i=20
while(i!=0):
    #if i%2==1:
     print(i)
     i-=1
i=1
while(i<3):
    print(i)
    i+=1

#floor and ceil value from user input
import math

floatt=input('Enter a floating point number : ')
f=float(floatt)
print(math.floor(f))
print(math.ceil(f))

#absolute value
a=int(input('first : '))
b=int(input('first : '))
c=int(input('first : '))
if a>0:
    print(a)
else:
    print(a*(-1))
    
if b>0:
    print(b)
else:
    print(b*(-1))
    
if c>0:
    print(c)
else:
    print(c*(-1))
    
#Rock, paper, scissor game
s=str(input('enter a string : '))
s1=str(input('enter another string : '))
if s=='paper' and s1=='scissor':
    print("second player win")
else:
    print("First player is winner")

#problem 3

while True:
    user_input = input("Enter input: ")
    
    if user_input.lower() == "quit":
        print("Program stopped.")
        break
    
    try:
        number = float(user_input)
        
        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print(f"{number} is zero.")
    except ValueError:
        print("Invalid input, please enter a number or type 'Quit' to exit.")

        
