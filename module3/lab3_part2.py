# Programmer name: Joseph Clark 
# 01/26/22 
# Lab 3: Decision Making - part 2

print("Welcome to the CMSY 156 Soccer Calculator!")

games = float(input("Enter the number of games: "))
shots = float(input("Enter the number of shots taken: "))
goals = float(input("Enter the number of goals made: "))

average_goals = goals / games
average_shots = shots / games
average_shots = shots / goals

print(f"The average goals per game is : {average_goals:>,.2f}")
print(f"The average shots per game is: {average_shots:>,.2f}")
print(f"The average shots per goal is: {average_shots:>,.2f}")

print("Thank you for using this program!")  