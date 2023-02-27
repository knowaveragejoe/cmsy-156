# CMSY-156
# Programmer name: Joseph Clark 
# 02/2/22 
# Lab 6: Files part 1

# Given an input type, prompts the user and validates their input
def prompt_and_validate_input(input_type):
    user_input = input("Enter the number of " + input_type + ": ")
    if not user_input.isnumeric() or not float(user_input) >= 0:
        print ("Error - " + input_type + " cannot be negative. Please reenter")
        return False
    else:
        return float(user_input)

print("Welcome to the CMSY 156 Soccer Calculator!")

names = []

# Open file
file = open("soccer.txt", "r")
# Read lines
for line in file:
    names.append(line[:-1])

# Close file
file.close()

# Print names from the file
print(f"First name: {names[0]:>20}")
print(f"Last name: {names[1]:>20}")
print(f"Team name: {names[2]:>20}")
print(f"League name: {names[3]:>20}")

print ("Enter the info for " + names[0] + " " + names[1])

# Repeat taking input until user exits gracefully
while (True):
  # Gather number of games, print error or convert to float
  games = prompt_and_validate_input("games")
  while not games:
      print("Number of games must be greater than 0. Try again")
      games = prompt_and_validate_input("games")

  # Gather number of shots taken, print error or convert to float
  shots = prompt_and_validate_input("shots taken")
  while not shots:
      print("Number of shots takens must be greater than 0. Try again")
      shots = prompt_and_validate_input("shots taken")
      
  # Gather number of goals, print error or convert to float
  goals = prompt_and_validate_input("goals")
  while not goals:
      print("Number of goals must be greater than 0. Try again")
      goals = prompt_and_validate_input("goals")

  # if games or shots on goal is 0, answers will naturally be 0
  if (games == 0 or shots == 0):
      print("The average goals per game is: 0.0")
      print("The average shots per game is: 0.0")
      print("The average shots per goal is: 0.0")
  else:
      # Ensure shots per goal is 0 if no goals were scored
      if (goals == 0):
          average_shots_per_goal = 0.0
      else:
          average_shots_per_goal = shots / goals
      # Perform our calculations
      average_goals = goals / games
      average_shots_per_game = shots / games

      # Print calculation results
      print(f"The average goals per game is: {average_goals:>20,.2f}")
      print(f"The average shots per game is: {average_shots_per_game:>20,.2f}")
      print(f"The average shots per goal is: {average_shots_per_goal:>20,.2f}")

      # Ask if the user wants to continue
      another = input("Would you like to enter another (y/n)? ")
      while (another not in ["Y", "y", "N", "n"]):
          print("Invalid input, please try again.")
          another = input("Would you like to enter another (y/n)? ")
              
      # Control whether to continue or not
      if (another == "N" or another == "n"):
          break

print("Thank you for using this program!")  