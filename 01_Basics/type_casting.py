# ==========================================
# TYPE CASTING IN PYTHON
# ==========================================

# String to Integer
num = "25"
print("Original:", num, type(num))

num = int(num)
print("After int():", num, type(num))

print("--------------------------------")

# Integer to Float
marks = 90
marks = float(marks)
print(marks, type(marks))

print("--------------------------------")

# Float to Integer
price = 99.99
price = int(price)
print(price, type(price))

print("--------------------------------")

# Integer to String
age = 19
age = str(age)
print(age, type(age))

print("--------------------------------")

# User Input Type Casting

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)