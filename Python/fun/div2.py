n = input("Divisors:")
n = float(n)
i = 1
divisors = [0]
order_divisors = []
while (i <= n **0.5):
    if (n % i == 0) :
        divisors.append(i)
        a = n // i
        int(i)
        int(a)
        divisors.append(a)
        order_divisors = sorted(divisors)

    i = i + 1
print(order_divisors)
print("")
print ("end")
