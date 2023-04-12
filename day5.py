# warmup
global checkingAcct
checkingAcct = 200

print("")

# if user responds no
def responseIsNo():
    return "Okay, you selected \"NO\""

# performs a deposit on user's acct
def deposit(account):
    # gets amount to deposit
    try:
        value = int(input("How much would you like to deposit?: "))
    except(ValueError):
        print("Invalid Input")

    # adds deposit to account
    account += value
    print("%s is being deposited into your account." % str(value))
    return account

def withdraw(account):
    # gets amount to withdraw
    try:
        value = int(input("How much would you like to withdraw?: "))
    except(ValueError):
        print("Invalid Input")
    
    # checks for overdraft
    if account < value:
        print("You are trying to withdraw more than your account has. \nPlease restart and try again.")
        return 
    elif value < account:
        account -= value

    print("%s is being withdrawn from your account." % str(value))
    return account

# checks if user would like to withdraw
try:
    withdrawQuery = str(input("Would you like to withdraw any money?[YES/NO]: ").upper())
except(ValueError):
    print("Inalid Input")

# processes user's WITHDRAWAL input
if withdrawQuery == 'YES':
    checkingAcct = withdraw(checkingAcct)
    print("Your new balance is %s" % checkingAcct)
elif withdrawQuery == 'NO':
    print(responseIsNo())
else:
    print("Your input was not one of the options, \nplease restart and try again OR continue to deposit.")

# checks if user would like to deposit
try:
    depositQuery = str(input("Would you like to deposit any money?[YES/NO]: ").upper())
except(ValueError):
    print("Inalid Input")

# processes user's DEPOSIT input
if depositQuery == 'YES':
    checkingAcct= deposit(checkingAcct)
    print("Your new balance is %s" % checkingAcct)
elif depositQuery == 'NO':
    print(responseIsNo())
else:
    print("Your input was not one of the options, please restart and try again.")

print(" Thank you for banking with the Bank of Aadil.")