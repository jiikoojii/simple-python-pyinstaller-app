import random
min = 0
max = 1000

x = random.randint(min, max)
y = random.randint(min, max)
z = random.randint(1, 4)

print("first number:", z, "\nsecond number:", y, "\noperator:", z)
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
def operations(z):
	switcher={
		1: print(x, "+" ,y, "=", add(x, y)),
		2: print(x, "-", y, "=", subtract(x, y)),
		3: print(x, "*", y, "=", multiply(x, y)),
		4: print(z, "/", y, "=", divide(x, y)),
}