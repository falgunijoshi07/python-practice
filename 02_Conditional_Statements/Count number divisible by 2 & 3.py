# Program: Count Numbers Divisible by 2 and 3
# Description:
# Take an integer n as input.
# Count how many numbers from 1 to n
# are divisible by both 2 and 3,
# then print the count.

n=int(input("enter a number:"))
count=0
for i in range (1,n+1):
    if i % 2 == 0 and i % 3 == 0:
        count=count + 1
print (count)