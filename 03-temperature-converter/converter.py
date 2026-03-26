"""
Temperature Converter - Project 03
----------------------------------
What it does: Converts temperatures between Celsius, Fahrenheit, and Kelvin. 
Uses three separate conversion functions and a menu to pick the direction. 
Displays results neatly formatted to two decimal places.

Pro Hints:
- We keep our mathematical logic separate in 'pure' functions that just convert and return.
- We use a main loop and f-string formatting (`:.2f`) to cleanly display float results.
"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def converter():
    print("Welcome to the Temperature Converter!")
    
    while True:
        print("\nChoose an option:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Quit")
        
        choice = input("> ")
        
        if choice == '5' or choice.lower() == 'q':
            print("Exiting converter. Stay temperate!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please pick a number 1-5.")
            continue
            
        try:
            temp = float(input("Enter the temperature value directly: "))
        except ValueError:
            print("Invalid number! Please enter a numeric temperature.")
            continue
            
        # Dispatch the appropriate function based on choice
        if choice == '1':
            res = celsius_to_fahrenheit(temp)
            print(f"Result: {temp} Celsius is {res:.2f} Fahrenheit")
        elif choice == '2':
            res = fahrenheit_to_celsius(temp)
            print(f"Result: {temp} Fahrenheit is {res:.2f} Celsius")
        elif choice == '3':
            res = celsius_to_kelvin(temp)
            print(f"Result: {temp} Celsius is {res:.2f} Kelvin")
        elif choice == '4':
            res = kelvin_to_celsius(temp)
            print(f"Result: {temp} Kelvin is {res:.2f} Celsius")

if __name__ == "__main__":
    converter()
