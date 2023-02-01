# Programmer name: Joseph Clark 
# 01/29/22 
# Lab 3: Decision Making - part 1.5

print("Welcome to the CMSY 156 Soccer Calculator!")

# Collect user input and handle 0-cases
games = float(input("Enter the number of games: "))
shots = float(input("Enter the number of shots taken: "))
if (games == 0 or shots == 0):
    print(f"The average goals per game is: 0.0")
    print(f"The average shots per game is: 0.0")
    print(f"The average shots per goal is: 0.0")
    exit()
goals = float(input("Enter the number of goals made: "))

# Ensure shots per goal is 0 if no goals were scored
if (goals == 0):
    average_shots_per_goal = 0.0
else:
    average_shots_per_goal = shots / goals

# Calculate other averages
average_goals = goals / games
average_shots_per_game = shots / games

# Print output
print(f"The average goals per game is: {average_goals:>20,.2f}")
print(f"The average shots per game is: {average_shots_per_game:>20,.2f}")
print(f"The average shots per goal is: {average_shots_per_goal:>20,.2f}")

print("Thank you for using this program!")  