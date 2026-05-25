import random
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist,k=2))
#range
x=range(10000000)
y=random.sample(x,k=100000)
print(y)