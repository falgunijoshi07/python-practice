# ==========================================
# IF ELSE STATEMENTS
# ==========================================

# Program 1 - Check if number is positive

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
else:
    print("Zero or Negative Number")

print("--------------------------------")

# Program 2 - Check if person can vote

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

print("--------------------------------")

# Program 3 - Check if number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")