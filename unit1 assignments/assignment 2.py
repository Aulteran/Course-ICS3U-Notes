# customer balance
balance = 1000

# determines minimum payment
def minPayment(bal):
    # checks if 2.1% of balance is greater than $10
    if 10 < bal*0.021:
        return bal*0.021
    else:
        return 10

print("Minimum Payment: %i" % minPayment(balance))