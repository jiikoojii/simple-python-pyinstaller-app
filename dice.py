import random
min = 1
max = 1000

x = random.randint(min, max)
y = random.randint(min, max)
z = random.randint(1, 4)
#if (number < 50):
#	print("Okay so basically am very smol only ", #number)
#else:
#	print("Not so smol anymoar with ", number)
#print(number)
print(z, y, z)
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y

if z == 1:
	print(x "+" y, add(x, y))
elif z == 2:	
	print(x "-" y, subtract(x, y))
elif z == 3:	
	print(x "*" y, multiply(x, y))
elif z == 4:	
	print(z "/" y, divide(x, y))