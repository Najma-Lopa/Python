#break and continue
num=0
while(num<10): 
    num+=1 #eivabe gap deoyar nam hoilo indentation;
    if(num==8):
     continue
    print(num)
   
   # if(num==5):
       # break
       
#for loop
numbers=[1,3,4,5,6,7,8]
sum=0
for num in numbers:
    print(num)
    sum+=num
print(sum)

#another
for i in range(1,10,2): #eikhane 1 start,10 er age porjonto, 2 kore barbe
    print(i)