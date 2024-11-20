
#numbers=[12,13,14,15,16,50]
#total=sum(numbers)
#print(total)
num={1,2,3,4,5}
totall=0
for i in num:
    totall+=i #set er jnno
print(totall)

for i in num:
    print(i) # শুধু নাম্বার পাওয়ার জন্য
for i in enumerate(num): #নাম্বার এর সাথে ইন্ডেক্স পাওয়ার জন্য এটা
    print(i)
    
#or
for i,nums in enumerate(num): #নাম্বার এর সাথে ইন্ডেক্স পাওয়ার জন্য এটা
    print(i,nums)

'''
marks={'physics': 12,'chemistry': 45,'math':56}
for mark in marks:
    val=marks[mark]
    print(mark,val)

#or 

for subject, mark in marks.items():
    print(subject,mark)
    
# for mark in marks:
#     val=marks['math']
#     print(mark,val)
'''