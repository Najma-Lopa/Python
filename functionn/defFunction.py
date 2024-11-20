def double_it(num):
    result=num*2
    print(result)
double_it(50)

def add(num1, num2):
    ans=num1+num2
    return ans
res=add(20,30)
print(res)

def mul(num1, num2):
    ans=num1+num2
    print(f'num1= {num1} and num2={num2}')
    return ans #রিটার্ন টাইপ
ress=mul(num2=20,num1=30) # এইখানে ফাংশন এর নাম্বার গুলাকে চেঞ্জ করে দিতে পারি। A কে আগে এবং B কে পরে
print(ress)

def multuply2(*numbers):
#এইখানে স্টার দেওয়ার জন্য সব নাম্বার একেবারে এক্সেস করতে পারে
#এই স্টার টার নাম হইলো টাপল
#যতগুলা প্যারামিটার পাঠাই না কেন সব নিয়ে নিবে।
    # print(numbers)
    for num in numbers:
        print(num)
final_result=multuply2(12,3,44)

def dif(num, *numbers):
    print(num)
    print(numbers)
dif(2,3,4,5,6)


def full_name(f_name,last_name):
    nam=f'{f_name} {last_name}'
    print(nam)
full_name(f_name='najma', last_name='Lopa')


""" Karg er implimentation 
string er touple neoyar jnno double star neoya lage
"""
def full_nam(**kargs):
    print(kargs)
full_nam(first='najma', last='Lopa')
