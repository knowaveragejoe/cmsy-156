# Programmer name: Joseph Clark 
# 01/26/22 
# Lab 4: Repetition part 2

# Constants
absolute_zero = -273.15

# Ask for a starting temp and either print an error and convert to float
starting_temp = input("Enter a starting temperature: ")
while not starting_temp or float(starting_temp) < absolute_zero:
    print(f"Starting temperature invalid, must be greater than absolute zero({absolute_zero})")
    starting_temp = input("Enter a starting temperature: ")
starting_temp = float(starting_temp)

# initialize our "counter" temperature variable
current_temp = starting_temp

print("Temperature conversions using a while loop:")
print("Cels Fahr Kelvin")
while current_temp <= (starting_temp + 19):
    fahrenheit = (9/5) * current_temp + 32
    kelvin = current_temp + 273.15
    print(f"{current_temp:.2f} {fahrenheit:.2f} {kelvin:.2f}")
    current_temp += 1

# Reset our counter temperature
current_temp = starting_temp

print("Temperature conversions using a for loop:")
print("Cels Fahr Kelvin")
for i in range(int(starting_temp), int(starting_temp) + 20):
    fahrenheit = (9/5) * current_temp + 32
    kelvin = current_temp + 273.15
    print(f"{current_temp:.2f} {fahrenheit:.2f} {kelvin:.2f}")
    current_temp += 1