# Programmer name: Joseph Clark 
# 01/26/22 
# Lab 4: Repetition part 1.5

print("Welcome to the CMSY 156 Soccer Calculator!")

# Repeat taking input until user exits gracefully
while (True):
    # Gather number of games, print error or convert to float
    games = input("Enter the number of games: ")
    while not games or not games.isnumeric() or float(games) <= 0:
        print("Number of games must be greater than 0. Try again")
        games = input("Enter the number of games: ")
    games = float(games)

    # Gather number of shots taken, print error or convert to float
    shots = input("Enter the number of shots taken: ")
    while not shots or not shots.isnumeric() or float(shots) <= 0:
        print("Number of shots takens must be greater than 0. Try again")
        shots = input("Enter the number of shots taken: ")
    shots = float(shots)
        
    # Gather number of goals, print error or convert to float
    goals = input("Enter the number of goals: ")
    while not goals or not goals.isnumeric() or float(goals) <= 0:
        print("Number of goals must be greater than 0. Try again")
        goals = input("Enter the number of goals: ")
    goals = float(goals)

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