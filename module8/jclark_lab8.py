# CMSY-156
# Programmer name: Joseph Clark 
# 02/27/22 
# Lab 7: Strings

def main():
    # Prompt the user for a filename and attempt to open it continuously until a valid filename is entered
    while True:
      filename = input("Enter the path to the file: ")
      try:
          file_descriptor = open_file(filename)
          break
      except:
          print("Error opening file. Please try again")

    # Read the file and append each line to a list
    foods = []
    for line in file_descriptor:
       foods.append(line)
    
    # Create statistics for the - total items, items containing "pizza" and items containing "burger"
    total_foods = len(foods)

    total_pizzas = 0
    for food in foods:
      if "pizza" in food:
        total_pizzas += 1
    
    total_burgers = 0 
    for food in foods:
      if "burger" in food:
        total_burgers += 1
    
    # Extract the prices from each line & calculate the sub total
    sub_total = 0
    for food in foods:
      sub_total += float(food[16:])
    
    # Calculate tax & grand total
    tax = sub_total * 0.06
    grand_total = sub_total + tax

    # Display final output
    print ("Output Report: ")
    print ("---------------")

    print ("The total number of items sold is: ", total_foods)
    print ("Total number of items with pizza is: ", total_pizzas)
    print ("Total number of items with burger is: ", total_burgers)

    print (""""
      Food Item          Amount Sold
      ---------          -----------
    """)

    for food in foods:
      print (food[:16], f"${float(food[16:]):,.2f}")
    
    print ("The subtotal sold is: ", f"${sub_total:,.2f}")
    print ("The total tax is: ", f"${tax:,.2f}")
    print ("The grand total collected for the night is: ", f"${grand_total:,.2f}")

    print ("Program complete!")

    # Close the file 
    file_descriptor.close()


# Opens the file and returns the file descriptor
def open_file(filename):
  file = open(filename, "r")
  return file

main()