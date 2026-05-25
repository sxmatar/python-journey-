import random

print(random.random())
#Random int
y=int(input("Guess a number"))
x=random.randint(0,20)
print(x)
#numbguessinggame
if (y==x):{
    print("correct answer")
}

else:{
    print("try again")
}