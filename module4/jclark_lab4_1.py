# CMSY-156
# Programmer name: Joseph Clark 
# 02/02/22 
# Lab 3: Decision Making - part 1

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
        print("Error: Please enter 1 or 2. Try again!")

# Collect address if delivery selected & add delivery charge
delivery_address = ""
if (delivery_method == "1"):
    total += 5.00
    delivery_address = input("Enter the delivery address: ")

# Collect tip and add to total if valid
tip_is_valid = False
while (not tip_is_valid):
    tip = input("Please enter the amount of the tip: $")
    if (not tip or not tip.isnumeric()):
        print("Tip entered is invalid. Please try again")
    else:
        tip_is_valid = True
        total += float(tip)

# Begin collecting order info
print("What would you like to order today?")

# Accumulate pizza orders, if the user selects checkout break out of the loop
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
    
    # Accumulate pizza orders, ff the user selects checkout we break out of loop
    if (pizza_selection == "4"):
        break
    else:
        if (pizza_selection == "1"):
            pizza_cost = 11.50
        elif (pizza_selection == "2"):
            pizza_cost = 12.50
        elif (pizza_selection == "3"):
            pizza_cost = 13.50
        else:
            print("Error: please enter a valid menu option. Try again!")
            continue
        
        pizza_total += pizza_cost

# Calculate tax & final total
tax = pizza_total * 0.06
total = total + pizza_total + tax

# Display output & end interaction with user
if (delivery_method == "1"):
    print(f"The total cost with tax, tip and delivery charge is: ${total:,.2f}")
    print("Delivery address: " + delivery_address)
else:
    print(f"The total cost with tax and tip is: ${total:,.2f}")

print("Thank you for coming to the CMSY-156 pizza shop. Please come again!")