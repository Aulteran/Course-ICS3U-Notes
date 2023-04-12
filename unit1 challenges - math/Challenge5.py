# Challenge 5
# Write a program that converts one unit of measurement to another (ie. 
# Degrees Fahrenheit, to degrees Celsius)

def toFahrenheit(c):
    return (c - 32) * (5 / 9)

def toCelcius(f):
    return (f * 9 / 5) + 32

def toKelvin(c):
    return c + 273.15

print("Welcome to the temperature converter.")
print("Please enter the unit of measurement you wish to convert:")
print("1. Fahrenheit")
print("2. Celsius")
print("3. Kelvin")
choice = input("Enter your choice: ")
if choice == "1":
    print("You have selected Fahrenheit.")
    print("Enter the temperature in Fahrenheit: ")
    f = float(input())
    print("The temperature in Fahrenheit is: " + str(f))
    print("The temperature in Celsius is: " + str(toCelcius(f)))
    print("The temperature in Kelvin is: " + str(toKelvin(toCelcius(f))))
elif choice == "2":
    print("You have selected Celsius.")
    print("Enter the temperature in Celsius: ")
    c = float(input())
    print("The temperature in Fahrenheit is: " + str(toFahrenheit(c)))
    print("The temperature in Celsius is: " + str(c))
    print("The temperature in Kelvin is: " + str(toKelvin(c)))
elif choice == "3":
    print("You have selected Kelvin.")
    print("Enter the temperature in Kelvin: ")
    k = float(input())
    print("The temperature in Fahrenheit is: " + str(toFahrenheit(k-273.15)))
    print("The temperature in Celsius is: " + str(k-273.15))
    print("The temperature in Kelvin is: " + str(k))
