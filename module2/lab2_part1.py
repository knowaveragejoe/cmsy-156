# Programmer name: Joseph Clark 
# 01/31/22 
# Lab 2: Input, Output and Processing (Part 1)

print("Welcome to the CMSY 156 Soccer Calculator!")

# Take user input
games = int(input("Enter the number of games: "))
shots = int(input("Enter the number of shots taken: "))
goals = int(input("Enter the number of goals made: "))

# Perform our calculations
average_goals = goals / games
average_shots_per_game = shots / games
average_shots_per_goal = shots / goals

# Show output & exit
print("The average goals per game is : " + str(average_goals))
print("The average shots per game is: " + str(average_shots_per_game))
print("The average shots per goal is: " + str(average_shots_per_goal))
print("Thank you for using this program!")