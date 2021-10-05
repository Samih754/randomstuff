num = 0
average = 0
count = 0
sum = 0
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        numb = float(num)
    except :
        print('Invalid input')
        continue
    if smallest is None :
        smallest = numb
    elif numb < smallest :
        smallest = numb
    if largest is None:
        largest = numb
    if largest < numb :
        largest = numb
    elif numb > largest :
        largest = numb
    count = count + 1
    sum = sum + numb
    average = (sum / count)
    range = largest - smallest
    odds = sum / 1


print("                ")
print("The range is", range )
print("Maximum is", largest)
print("Minimum is", smallest)
print("There are:", count, "numbers.")
print("The sum is: ", sum)
print("the average is:", average)
print("The odds are", odds)
