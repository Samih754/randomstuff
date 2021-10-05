#Ok so basically this programm reunites both the find all divisors in a interval and also we can test to see if a number is prime or note
#each of them have a a function and they are called if we write  int   or  test to see if 1 is 1. And it breaks if ever smth else is typed

def test_prime():
    # Program to check if a number is prime or not

    # To take input from the user
    try:
        num = int(input("Enter a number: "))
    except:
        print("insert a number")
    # prime numbers are greater than 1
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print("")
               # ok so basically // is / but it makes it an interger and not a floating point number like the normal divide sign
               print(i,"times",num // i,"is",num)
               print("")
               break
       else:
           print("")
           print(num,"is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")

def all_prime():
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


while 1 < 2:
    print("")
    task = input("Press 'int' to see prime numbs in a interval, 'test' to see if a number is prime or type exit to exit: ")
    print("")
    if task == ("test"):
        test_prime()
    elif task == ("int"):
        all_prime()

    else:
        break


print("The end")
