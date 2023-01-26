# Programmer name: Joseph Clark 
# 01/26/22 
# Lab 3: Decision Making - part 2

# Collect user input
num_scoops = int(input("How many scoops would you like? "))
if (num_scoops <= 0):
    print("No scoops for you, exiting")
    exit()

waffle_cone = input("Would you like a waffle cone? ")

total = 0
price_per_scoop = 1.50
# Determine if volume discount applies
if (num_scoops >= 3):
    price_per_scoop = 1.25

# Determine if waffle cone charge applies
if (waffle_cone == "Y" or waffle_cone == "y"):
    total += 1.10

total += (price_per_scoop * num_scoops)

# Print costs
print(f"The price per scoop is: {price_per_scoop:,.2f}")
if (num_scoops == 1):
    print("You ordered 1 scoop")
else:
    print(f"You ordered {num_scoops} scoops")

print(f"Your total cost is ${total:,.2f}")
print("Thank you for using the program")