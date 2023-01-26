# Programmer name: Joseph Clark 
# 01/26/22 
# Lab 4: Repetition part 1

# Dictionary of pizza specifications to make things cleaner later
pizzas = {
    "1": { 
        "toppings": "Plain",
        "cost": 11.50
    },
    "2": {
        "toppings": "Veggie",
        "cost": 12.50
    },
    "3": {
        "toppings": "Pepperoni",
        "cost": 13.50
    }
}

print("Welcome to the CMSY-156 Pizza Shop!")

total = 0.00
sales_tax = 0.06
delivery_fee = 5.00

# Collect delivery method
delivery_method_valid = False
while (not delivery_method_valid):
    delivery_method = input("Enter 1 for delivery, 2 for pickup: ")
    if (delivery_method == "1" or delivery_method == "2"):
        delivery_method_valid = True
    else:
        print("Error: Please enter 1 or 2. Try again!")

# Collect delivery address and apply delivery fee if necessary
delivery_address = ""
if (delivery_method == "1"):
    total += delivery_fee
    delivery_address = input("Enter the delivery address: ")

# Collect pizza selection and accumulate costs
pizza_total = 0.00
pizza_type_valid = False
while (not pizza_type_valid):
    print("What would you like to order today?")
    print("""
        1. Plain Pizza
        2. Pepperoni Pizza
        3. Veggie Pizza
        4. Checkout
    """)
    pizza_selection = input("Enter your order here: ")
    
    # If the user selects checkout, break out of loop
    if (pizza_selection == "4"):
        break
    else:
        if (pizza_selection in pizzas):
            pizza_total += pizzas[pizza_selection]["cost"]
        else:
            print("Error: please enter a valid menu option. Try again!")

# Collect tip, if any
tip_is_valid = False
while (not tip_is_valid):
    tip = input("Please enter the amount of the tip: $")
    if (not tip or not tip.isnumeric()):
        print("Tip entered is invalid. Please try again")
    else:
        tip_is_valid = True
        total += float(tip)

# Calculate tax and add to total
tax = pizza_total * sales_tax
total += pizza_total + tax

if (delivery_method == "1"):
    print(f"The total cost with tax, tip and delivery charge is: ${total:,.2f}")
    print("Delivery address: " + delivery_address)
else:
    print(f"The total cost with tax and tip is: ${total:,.2f}")

print("Thank you for coming to the CMSY-156 pizza shop. Please come again!")