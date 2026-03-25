# Program to print Fibonacci numbers

# Number of terms
n = 10

# First two numbers
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
