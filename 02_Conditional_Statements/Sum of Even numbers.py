# Program: Sum of Even Numbers
# Description:
# Take an integer n as input.
# Find and print the sum of all even numbers
# from 1 to n.
 
n=int(input("Enter a number:"))
total=0
for i in range (1,n+1):
    if i % 2 == 0:
        total=total + i
print(total)
