#a is the smallest number of the range b is the biggets and c is the multiples we want

a = int(input("From where?: "))
b = int(input("To where?: "))
c = int(input("What multiples?: "))

#i var is all multiples of c between a an b (b+1 becaus the last numb is a crochet ouver so it doesnt count)
for i in range(a, b + 1 , c):
    print(i)
print("")
print("end")
