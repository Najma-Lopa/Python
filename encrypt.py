data="firebaby"
shift=4;
output=''
for char in data:
    output+=chr((ord(char)+shift-97)%26+97) #ord dile asci value peye zabo
print(output);

#reverse function
s=str(input("enter a string: "));
reverse=s[::-1]
print(reverse)