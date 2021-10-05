# Python program to display all the prime numbers within an interval

list = []
slist = []

lower = input("From?: ")
try:
    lower = int(lower)
except:
    print("put a number")
upper = input("To?:  ")
try:
    upper = int(upper)
except:
    print("Put a number")

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           list.append(num)

slist = sorted(list)
print("")
print(slist)
