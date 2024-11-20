import math
from math import ceil,sin
ans= sin(90)
res= ceil(ans)
print(res)
# print(ans)

#use of random
import random
num=random.random() # ০ থেকে ১ এর মাঝে দশমিক এর র‍্যানডম একটা সংখ্যা দিবে
num2=random.randint(2,5)
print(num)
print(num2)

#use of random choice from given list
import random as ran #as দিয়ে এটাকে ran হিসেবে ইউজ করতে পারি
num=ran.choice([2,3,4,5,6,7,8,9])
#আমার দেওয়া লিস্টের মধ্যে থেকে যেকোনো একটা ভ্যালু দিবে
print(num)
