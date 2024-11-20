numbers=[1,3,7,5,9,8,8,9]
'''
print(numbers[1])
print(numbers[-6])
#মাইনাস থেকে শুরু মানে পিছন থেকে -1 থেকে কাউন শুরু হবে 
#সামনে থেকে শুরু হলে ০ থেকে শুরু হবে ;
print(numbers[1:5]) # এইখানে ১ কোলন ৫ মানে ১ সহ ৫ এর আগে পর্যন্ত মানে ১,২,৩,৪;
print(numbers[1:]) #এইভাবে দিলে ১ থেকে শুরু করে শেষ পর্যন্ত যাবে;
print(numbers[2,6,2]) #এইখানে শেষের ২ মানে ২ করে করে বৃদ্ধি পাবে
print(numbers[:]) #এইভাবে ফুল এর‍্যে পাব
print(numbers[: :-1]) #ফুল এর‍্যে তার রিভার্জ ভার্ষন পাব

'''
'''
numbers.append(10)
print(numbers)
#numbers.remove(8)
print(numbers)
numbers.insert(3,12)
print(numbers)

'''
'''
x=numbers.count(8)
print(x)
numbers.sort() #assending order sort
print(numbers)
numbers.sort(reverse=True) # descending order sort
print(numbers)

'''

numbers=[12,45,56,45,12,89]
print(numbers)
#set
#set সবসময় ইউনিক ভ্যালু দিবে এটাকে
nums={12,45,56,45,12,89}
print(nums)