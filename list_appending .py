fruit = ["apple", "banana", "cherry","melon","watermelon","papaya"]
fruit2=["pomegranate","raspberries","sapota"]
num1= fruit+fruit2
print(num1)
num1.append("peach")
print(num1)
num1.append("rambutan")
print(num1)
#extend
fruit.extend(fruit2)
print(fruit)
#insert 
fruit.insert(1,"cherry")
print(fruit)
#count
x = fruit.count("cherry")
print(x)
#index
y = fruit.index("papaya")
print(y)