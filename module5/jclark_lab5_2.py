# CMSY-156
# Programmer name: Joseph Clark 
# 02/26/22 
# Lab 5: Functions part 2

ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67

# Main function
def main():
    menu()

# Converts a celcius temperature to fahrenheit
def to_fahr(ctemp):
  return (ctemp * 9/5) + 32
    
# Converts a fahrenheit temperature to celcius
def to_cels(ftemp):
  return (ftemp - 32) * 5/9

# Displays the menu and handles user input
def menu():
  print("Welcome to the CMSY 156 Temperature Converter!")

  # Repeat taking input until user exits
  while True:
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Quit")
    choice = input("Enter your choice: ")
    while not choice or not choice.isnumeric() or (not choice == "1" and not choice == "2" and not choice == "3"):
        print("Invalid choice, please try again.")
        choice = input("Enter your choice: ")
    
    if choice == "1":
        cels = input("Enter the temperature in Celsius: ")
        while not cels or not cels.isnumeric() or float(cels) < ABSOLUTE_ZERO_C:
            print("Invalid input, please try again.")
            cels = input("Enter the temperature in Celsius: ")
        cels = float(cels)

        fahr = to_fahr(cels)
        print(f"{cels:.2f} degrees Celsius is {fahr:.2f} degrees Fahrenheit.")
    elif choice == "2":
        fahr = input("Enter the temperature in Fahrenheit: ")
        while not fahr or not fahr.isnumeric() or float(fahr) < ABSOLUTE_ZERO_F:
            print("Invalid input, please try again.")
            fahr = input("Enter the temperature in Fahrenheit: ")
        fahr = float(fahr)

        cels = to_cels(fahr)
        print(f"{fahr:.2f} degrees Fahrenheit is {cels:.2f} degrees Celsius.")
    else:
        break

# Program entrypoint
main()

