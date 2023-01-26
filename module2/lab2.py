# Programmer name: Joseph Clark 
# 01/26/22 
# Lab 2: Input, Output and Processing (Part 2)

make_model = input("Enter the cellphone make and model: ")
phone_cost = float(input("Enter the price of the phone in dollars: "))
warranty_cost = float(input("Enter the price of the warranty in dollars: "))

subtotal = phone_cost + warranty_cost
sales_tax = subtotal * 0.06
shipping_cost = phone_cost * 0.017
total = sales_tax + shipping_cost + subtotal

print("Receipt:")
print("The cellphone purchase is: " + make_model)
print("The purchase price is: ${:,.2f}".format(phone_cost))
print("The warranty cost is: ${:,.2f}".format(warranty_cost))
print("The tax is: ${:,.2f}".format(sales_tax))
print("Shipping cost: ${:,.2f}".format(shipping_cost))
print("Total amount dude: ${:,.2f}".format(total))
