hour = input('Time?:')
hour = float(hour)
pay = input('Pay?:')
pay = float(pay)
def computepay(time, pay):
    if time > 40:
        extra = time - 40
        extrapay = pay * 1.5
    Pay = 40 * pay + extra * extrapay
    return Pay
payy = computepay(hour, pay)
print("Pay", payy)
