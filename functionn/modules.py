#অন্য ফাইল এর ফাংশন এই ফাইলে এক্সেস করার জন্য 
import defFunction
sum=defFunction.add(39,40)
print(sum)

#or
from defFunction import add
resss=add(3,4)
print(resss)

#sobgulake access korte caile
from defFunction import *
resss=add(3,4)
print(resss)