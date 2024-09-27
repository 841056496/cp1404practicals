"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
MENU =  C - Convert Celsius to Fahrenheit
        F - Convert Fahrenheit to Celsius

print MENU

GET choice
while choice != "Q":
    if choice == "C":
    Get celsius
    fahrenheit = celsius_to_fahrenheit()
    print fahrenheit

    if choice == "F":
    Get fahrenheit
    celsius = fahrenheit_to_celsius()
    print celsius

    else:
        print error
    print MENU
    Get choice
print("Thank you.")

celsius_to_fahrenheit() function
    return celsius * 9.0 / 5 + 32

fahrenheit_to_celsius() function
    return 5 / 9 * (fahrenheit - 32)
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
