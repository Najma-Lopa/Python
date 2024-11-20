'''
numbers=[12,23,3,5,4,23,22]
odd_numbers=[]
for num in numbers:
    if num%2==1:
        odd_numbers.append(num)
print(odd_numbers)
#or
odd_numbers2=[num for num in numbers if num%2==1 if num%5==0] #eivabe onek shorto dite pari
print(odd_numbers2)

'''

#use of nested for loop in one line
names=['sakin','sakib','salman']
ages=[37,32,21]
pairs=[(name,age) for name in names for age in ages]
print(pairs)