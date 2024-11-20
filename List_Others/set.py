number=[12,45,33,12,33,45,70]
# second bracket dile eta set hisebe kaj korbe and unique value dibe
numbers=set(number)
print(numbers)
numbers.add(12)
#যেহেতু ১২ একবার আছে তাই আর নতুন করে অ্যাড হবে না
print(numbers)
numbers.remove(70)
print(numbers)
print(len(numbers))