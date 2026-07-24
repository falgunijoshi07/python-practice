# Program: FizzBuzz
# Description:
# Print numbers from 1 to n.
# Print "Fizz" if divisible by 3,
# "Buzz" if divisible by 5,
# and "FizzBuzz" if divisible by both.

n=int(input("Enetr a number:"))
for i in range(1,n+1):
    if i % 3 == 0 and i % 5== 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)  