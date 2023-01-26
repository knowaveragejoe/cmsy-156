# Programmer name: Joseph Clark 
# 01/26/22 
# Lab 3: Decision Making - part 1

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

# Collect user input
print("What would you like to order today?")
pizza_type = input("Enter 1 for a plain pizza, 2 for a pepperoni pizza, 3 for a veggie pizza: ")
delivery_method = input("Enter 1 for delivery, 2 for pickup: ")
delivery_address = ""
if (delivery_method == "1"):
    delivery_address = input("Enter the delivery address: ")
tip = float(input("Please enter an amount to tip: $"))

# Calculate tax
tax = pizzas[pizza_type]["cost"] * 0.06
total = tax + pizzas[pizza_type]["cost"]

# Add delivery charge if necessary
if (delivery_method == "1"):
    total += 5.00

# Add tip if one given
if (tip):
    total += tip

print("You ordered a: " + pizzas[pizza_type]["toppings"] + " pizza")

if (delivery_method == "1"):
    print(f"The total cost with tax, tip and delivery charge is: ${total:,.2f}")
    print("Delivery address: " + delivery_address)
else:
    print(f"The total cost with tax and tip is: ${total:,.2f}")

print("Thank you for coming to the CMSY-156 pizza shop. Please come again!")