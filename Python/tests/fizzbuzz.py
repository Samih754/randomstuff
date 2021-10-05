#Fizzbuzz if i is a multiple of 3 it says fIZZ if its a multiple of 5 it says Buzz and if its a muliple of both it says Fizzbuzz
upper = int(input("Until where?: "))

for i in range(1, upper):
    #cvhecks for both
    if (i % 3) == 0 and (i % 5) == 0:
        print("Fizzbuzz")
        #if i is a ddivisor of 3 it prints Fizz
    elif (i % 3) == 0:
        print("Fizz")
#if 5 is a divisor of i it brints buzz
    elif (i % 5) == 0:
         print("Buzz")
    else:
    # prints i
        print(i)

print("end")
