n = input("Divisors:")
n = float(n)
i = 1
while (i <= n **0.5):
    if (n % i == 0) :
        print(i)
        print(n / i)

    i = i + 1
print ("end")
