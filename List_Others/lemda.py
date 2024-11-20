# def square(x):
#     return x*x
square=lambda x: x*x #উপরের দুই লাইনের কাজ এই এক লাইন করে ফেলে
result= square(6)
print(result)

add=lambda x,y: x+y
sum=add(45,5)
print(sum)

numbers=[12,13,2,4,5,6,67]
# nnumber gulake 2 diye gun kore output dibe
 
def double(x):
    return x*2
#or
double_its=lambda x:x*2
#or
#double_numbers=map(double,numbers)
#etar iteration er or hbe nicer vabeo direct
double_numbers=map(lambda x:x*2,numbers)
print(numbers)
print(list(double_numbers))

#use of filter
bigger_numbers=filter(lambda n:n>10,numbers)
print(list(bigger_numbers))

#dictionary te filter
actors=[
    {'name': 'sakib','age':34},
    {'name': 'sakin','age':50},
    {'name': 'ibne','age':65},
    {'name': 'sabana','age':30},
       ]
senior_actors=filter(lambda actor:actor['age']>35,actors)
print(list(senior_actors))

