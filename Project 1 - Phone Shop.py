__author__ = "Aadil Hussain"

package = None
total_cost = 0
additional_monthly_costs = 0

# Database of 
# package and accessory details.
packages = {
    'McBasic': {
        'name': 'McBasic Package',
        'phone_cost': 50,
        'included_storage': 2,
        'storage_options': None,
        'extra_diamonds': None,
        'cloud_data_backup': None,
        'monthly_insurance': 1
    },
    'Average Joe': {
        'name': 'Average Joe',
        'phone_cost': 150,
        'included_storage': 8,
        'storage_options': {
            '64GB': 200,
            '128GB': 350,
        },
        'extra_diamonds': None,
        'cloud_data_backup': {
            '1 year': 20,
            '2 years': 35
        },
        'monthly_insurance': 5
    },
    'Rich Kid Pro': {
        'name': 'Rich Kid Pro',
        'phone_cost': 800,
        'included_storage': 32,
        'storage_options': {
            '64GB': 200,
            '128GB': 350,
        },
        'extra_diamonds': 200,
        'cloud_data_backup': {
            '1 year': 20,
            '2 years': 35
        },
        'monthly_insurance': 20
    }
}
accessories = {
    'protective_case': {
        'rubber_case': 20,
        'carbon_fibre_case': 100,
    },
    'battery_charger': 100
}
dataPackages = {
    'Pay as you go': 0,
    '1 GB': 10,
    '2 GB': 15,
    '5 GB': 40,
    '20 GB': 150
}

# gets int/float inputs without error
def numQuery(prompt):
    try:
        return float(input(prompt))
    except(ValueError):
        print("invalid input")

# func intended to show details of packages to user
# didn't finish cause too lazy + not required
# raised exception incase anyone uses it.
def showPackageDetails():
    raise NotImplementedError

# takes package selected as parameter and prompts user with appropriate customization options.
def packageCustomizer(package):
    global total_cost
    global packages

    # shows what user can customize with selected package
    if package == 'McBasic':
        print('''
McBasic Package:
No customization options available for this package.''')
        return
    
    elif package == 'Average Joe':
        print('''
Average Joe Package:
You can customize:
- Additional Storage
- Cloud Data Backup''')
        
        # prompts user for extra storage, cloud backup, and/or diamonds depending on package
        addedStorage = numQuery('''
Would you like Additonal Storage?:
1. 64GB ($%i)
2. 128GB ($%i)
3. No Additional Storage
Select Here: '''%(((packages[package])['storage_options'])['64GB'], ((packages[package])['storage_options'])['128GB']))
        cloudDataBackup = numQuery('''
Would you like Cloud Data Backup?:
1. 1 Year Backups ($%i)
2. 2 Years Backups ($%i)
3. No Cloud Data Backup
Select Here: '''%(((packages[package])['cloud_data_backup'])['1 year'], ((packages[package])['cloud_data_backup'])['2 years']))
    elif package == 'Rich Kid Pro':
        print('''
Rich Kid Pro Package:
You can customize:
- Additional Storage
- Extra Diamonds
- Cloud Data Backup''')
        
        addedStorage = numQuery('''
Would you like Additonal Storage?:
1. 64GB ($%i)
2. 128GB ($%i)
3. No Additional Storage
Select Here: '''%(((packages[package])['storage_options'])['64GB'], ((packages[package])['storage_options'])['128GB']))
        cloudDataBackup = numQuery('''
Would you like Cloud Data Backup?:
1. 1 Year Backups ($%i)
2. 2 Years Backups ($%i)
3. No Additional Cloud Backup
Select Here: '''%(((packages[package])['cloud_data_backup'])['1 year'], ((packages[package])['cloud_data_backup'])['2 years']))
        addedDiamonds = numQuery('''
Would you like Extra Diamonds?:
1. Add Extra Diamonds ($%i)
2. No Extra Diamonds
Select Here: '''%((packages[package])['extra_diamonds']))
    else:
        print("inavalid package selection. application could not complete.")
        quit()
    
    if addedStorage == 1:
        total_cost += ((packages[package])['storage_options'])['64GB']
    elif addedStorage == 2:
        total_cost += ((packages[package])['storage_options'])['128GB']
    elif addedStorage == 3:
        total_cost += 0
    else:
        print("invalid storage selection. application could not complete.")
        quit()

    if cloudDataBackup == 1:
        total_cost += ((packages[package])['cloud_data_backup'])['1 year']
    elif cloudDataBackup == 2:
        total_cost += ((packages[package])['cloud_data_backup'])['2 years']
    elif cloudDataBackup == 3:
        total_cost += 0
    else:
        print("invalid cloud data backup selection. application could not complete.")
        quit()
    if cloudDataBackup <= 3 and cloudDataBackup >= 1:
        cloudDataEmail = input("What is the email you want to add to setup cloud data backup")
    
    if addedDiamonds == 1:
        total_cost += ((packages[package])['extra_diamonds'])
    elif addedDiamonds == 2:
        total_cost += 0
    else:
        print("invalid extra diamonds selection. application could not complete.")
        quit()
    
    print("Thank You, you've finished customizing your desired package.\n")

def add_ons():
    global total_cost
    global accessories

    # loop through carbon-case accessory selection until user selects valid option
    while True:
        fibre_case = input("Would you like a carbon fibre phone case for $%i?[YES/NO]: " %(accessories['protective_case'])['carbon_fibre_case']).upper()
        if fibre_case == 'YES':
            total_cost += ((accessories['protective_case'])['carbon_fibre_case'])
            break

        # if no carbon case, then loop until user selects valid option for rubber case
        elif fibre_case == 'NO':
            while True:
                rubber_case = input("Would you like a rubber phone case for $%i?[YES/NO]: " %(accessories['protective_case'])['rubber_case']).upper()
                if rubber_case == 'YES':
                    total_cost += ((accessories['protective_case'])['rubber_case'])
                    break
                elif rubber_case == 'NO':
                    total_cost += 0
                    break
                else:
                    print("invalid input.")
            break
        else:
            print("invalid input.")

    # loops through option for extra battery charger until valid option chosen
    while True:
        battery_charger = input("Would you like an extra fast battery charger for $%i?[YES/NO]: " %accessories['battery_charger']).upper()
        if battery_charger == 'YES':
            total_cost += (accessories['battery_charger'])
            break
        elif battery_charger == 'NO':
            total_cost += 0
            break
        else:
            print("invalid input.")

    print("You have completed the add-on accesories section.\n")
    return

def tradeInProgram():
    global total_cost
    print("We offer a $40 discount when you trade in an older phone.")

    # loops through until user selects valid trade in option
    while True:
        tradeInQuery = input("Would you like to trade in an older phone?[YES/NO]: ").upper()
        if tradeInQuery == 'YES':
            total_cost -= 40
            print("We have deducted $40 from your subtotal.")
            break
        elif tradeInQuery == 'NO':
            print("Trade in declined.\n")
            break
        else:
            print("invalid input.")

def phoneInsurance(package):
    global additional_monthly_costs
    print("We offer insurance on all our devices aswell.")
    print("For your package, the monthly charge for insurance is: $%i" %(packages[package])['monthly_insurance'])
    
    # loops though until user selects valid insurance optio
    while True:
        insuranceQuery = input("Would you like to have insurance?[YES/NO]: ").upper()
        if insuranceQuery == 'YES':
            additional_monthly_costs += (packages[package])['monthly_insurance']
            print("Insurance added for $%i.\n" %(packages[package])['monthly_insurance'])
            break
        elif insuranceQuery == 'NO':
            print("Insurance declined.\n")
            break
        else:
            print("invalid input.\n")

def dataPlan():
    global additional_monthly_costs
    global dataPackages
    
    # displays data packages avail
    print("We also offer data packages, as priced below:")
    print('''
    1) $%i - Pay as you go:
    2) $%i - 1 GB
    3) $%i - 2 GB
    4) $%i - 5 GB
    5) $%i - 20 GB
    6) Skip Data Packages''' %(dataPackages['Pay as you go'], dataPackages['1 GB'], dataPackages['2 GB'], dataPackages['5 GB'], dataPackages['20 GB']))
    
    # loops until user selects valid data package, breaks out when selected.
    while True:
        dataPlanQuery = numQuery("Please make your selection: ")
        if dataPlanQuery == 1:
            additional_monthly_costs += dataPackages['Pay as you go']
            break
        elif dataPlanQuery == 2:
            additional_monthly_costs += dataPackages['1 GB']
            break
        elif dataPlanQuery == 3:
            additional_monthly_costs += dataPackages['2 GB']
            break
        elif dataPlanQuery == 4:
            additional_monthly_costs += dataPackages['5 GB']
            break
        elif dataPlanQuery == 5:
            additional_monthly_costs += dataPackages['20 GB']
            break
        elif dataPlanQuery == 6:
            print("You have chosen to skip data packages.")
            break
        else:
            print("invalid input.\n")

print("Welcome to Phone Shop!")

# Loops through menu for customer to see package details and choose package.
while True:
    package_selector = numQuery('''
Please choose a package:
1. McBasic Package
2. Average Joe Package
3. Rich Kid Pro Package
4. See Package Details
5. Exit

Select Here: ''')
    #breaks out of loop if package is selected or user exits program.
    if package_selector == 1:
        package = 'McBasic'
        break
    elif package_selector == 2:
        package = 'Average Joe'
        break
    elif package_selector == 3:
        package = 'Rich Kid Pro'
        break
    elif package_selector == 4:
        showPackageDetails()
    elif package_selector == 5:
        quit()

# Adds base package cost to total cost 
total_cost += (packages[package])['phone_cost']

# asks user for optional customizations to selected package
# and adds price of customizations to total cost
packageCustomizer(package)

# asks user for optional add-on accessories
add_ons()

# checks if user wants to trade in old phone
tradeInProgram()

# checks if user wants phone insurance
phoneInsurance(package)

# checks if user wants data package
dataPlan()

# final total cost output.
print('''
Application Complete.

INVOICE
Your total cost is: $%i
Your added monthly cost is: $%i'''
%(total_cost, additional_monthly_costs))