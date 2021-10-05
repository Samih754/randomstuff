bignumb = input("Prime number until where; ")
try:
    bignumb = int(bignumb)
except:
    print("Put a number pls")

#a is the divided n i the divisor and bignumb is untl whe do we search for the prime numbers
divided = 3
divisor = 2
prime = True
list = []
slist = []

while divided <= bignumb:
    #if ever a % n == 0 primebecomes false thus it breaks and adds iit to a list

    if prime is True:

        if divisor == divided:
            list.append(divided)
            if divided < bignumb:
                divided = divided + 1
                divisor = 2
                prime = True

        elif divided % divisor == 0:
            prime = False
            divided = divided + 1
            divisor = 2



        elif divided % divisor != 0:
            prime = True
            if divisor < divided:
                divisor = divisor + 1


    elif prime is False:
        divided = divided + 1
        divisor = 2
        prime = True

slist = sorted(list)
print(slist)
