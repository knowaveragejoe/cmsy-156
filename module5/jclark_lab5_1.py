# CMSY-156
# Programmer name: Joseph Clark 
# 02/02/22 
# Lab 5: Functions - part 1

# Constants
SALES_TAX = 0.06
PLAIN_COST = 11.50
PEPPERONI_COST = 12.50
VEGGIE_COST = 13.50

# Displays the pizza menu
def display_pizza_menu():
    print("""
        1. Plain Pizza
        2. Pepperoni Pizza
        3. Veggie Pizza
        4. Checkout
    """)

# Returns a human-readable string of what pizza the user selected
def display_pizza_selection(pizza_type):
    return "Plain Pizza" if pizza_type == "1" else "Pepperoni Pizza" if pizza_type == "2" else "Veggie Pizza" if pizza_type == "3" else "Invalid Pizza"

# Displays a generic error message
def display_error(error):
    return "There was an issue with your order: " + error

# Asks for a tip, then calculates totals and prints the receipt
def checkout(total, delivery_type, address): 
    # Collect tip and add to total if valid
    tip_is_valid = False
    while (not tip_is_valid):
        tip = input("Please enter the amount of the tip: $")
        if (not tip or not tip.isnumeric()):
            display_error("Tip entered is invalid. Please try again")
        else:
            tip_is_valid = True
            total += float(tip)
    
    # Calculate tax and add to total
    total += total * SALES_TAX
    
    # Display receipt
    if (delivery_method == "1"):
        print(f"The total cost with tax, tip and delivery charge is: ${total:,.2f}")
        print("Delivery address: " + delivery_address)
    else:
        print(f"The total cost with tax and tip is: ${total:,.2f}")

####### Actual program ########
print("Welcome to the CMSY-156 Pizza Shop!")

# Order total
total = 0.0

# Collect delivery method
delivery_method_valid = False
while (not delivery_method_valid):
    delivery_method = input("Enter 1 for delivery, 2 for pickup: ")
    if (delivery_method == "1" or delivery_method == "2"):
        delivery_method_valid = True
    else:
        display_error("Please enter 1 or 2. Try again!")

# Collect address if delivery selected & add delivery charge
delivery_address = ""
if (delivery_method == "1"):
    total += 5.00
    delivery_address = input("Enter the delivery address: ")

# Begin collecting order info
print("What would you like to order today?")

# Accumulate pizza orders, if the user selects checkout break out of the loop
pizza_total = 0.00
pizza_type_valid = False
while (not pizza_type_valid):
    print("What would you like to order today?")
    display_pizza_menu()
    pizza_selection = input("Enter your order here: ")
    
    # Accumulate pizza orders, ff the user selects checkout we break out of loop
    if (pizza_selection == "4"):
        break
    else:
        if (pizza_selection == "1"):
            pizza_cost = PLAIN_COST
        elif (pizza_selection == "2"):
            pizza_cost = PEPPERONI_COST
        elif (pizza_selection == "3"):
            pizza_cost = VEGGIE_COST
        else:
            display_error("Please enter a valid menu option. Try again!")
            continue
        
        pizza_total += pizza_cost

# Add the cost of the pizzas to our running total
total += pizza_cost

# Call checkout
checkout(total, delivery_method, delivery_address)

# Display exit message
print("Thank you for coming to the CMSY-156 pizza shop. Please come again!")