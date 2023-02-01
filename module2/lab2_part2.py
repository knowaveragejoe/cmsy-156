# Programmer name: Joseph Clark 
# 01/31/22 
# Lab 2: Input, Output and Processing (Part 2)

# Take user input
make_model = input("Enter the cellphone make and model: ")
phone_cost = float(input("Enter the price of the phone in dollars: "))
warranty_cost = float(input("Enter the price of the warranty in dollars: "))

# Perform our calculations
subtotal = phone_cost + warranty_cost
sales_tax = subtotal * 0.06
shipping_cost = phone_cost * 0.017
total = sales_tax + shipping_cost + subtotal

# PRint the receipt
print("Receipt:")
print("The cellphone purchase is: " + make_model)
print(f"The purchase price is: ${phone_cost:,.2f}")
print(f"The warranty cost is: ${warranty_cost:,.2f}")
print(f"The tax is: ${sales_tax:,.2f}")
print(f"Shipping cost: ${shipping_cost:,.2f}")
print(f"Total amount dude: ${total:,.2f}")
