hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rph:")
rph = float(rph)
if h < 40:
    pay = h * rph
    print(pay)
else:
    extra = h - 40
    float(extra)
    pay = 40 * rph + extra * (rph * 1.5)
    print(pay)
