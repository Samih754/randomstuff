time = input("How much time did you spend working?:")
rph =  input('what is your rate per hour.')
time = float(time)
rph = float(rph)
if time <= 36.0 :
    pay = time * rph
    print('Your revenue is:', pay)
else:
    time = 36
    timeplus = time - 36
    pay = (time * rph) + (rph * 2.5) * timeplus
    print("your pay is:", pay)
print('thank you for using this program')
