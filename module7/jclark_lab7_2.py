# CMSY-156
# Programmer name: Joseph Clark 
# 02/27/22 
# Lab 7: Lists part 2

# Main function
def main():
  print ("Welcome to the CMSY-156 Test Score Calculator!")

  # Gather the scores
  scores = input_scores()

  # Call functions depending on user choice continuously until user exits
  while True:
    # Prompt for user choice
    display_menu()

    choice = int(input("Enter your choice: "))
    while choice <= 0 or choice > 5:
        print("Error - choice must be between 1 and 5. Please reenter")
        choice = int(input("Enter your choice: "))

    if choice == 1:
      score_metrics(scores)
    if choice == 2:
      mine_scores(scores)
    if choice == 3:
      update_score(scores)
    if choice == 4:
      display_scores(scores)
    if choice == 5:
      print("Thank you for using the CMSY-156 Test Score Calculator!")
      break # exit the loop & end the program

# Display the scores in reverse order using a slice
def display_scores(scores):
  print ("Scores in reverse order:")
  for score in scores[::-1]:
    print(f"{score:>20,.2f}")

# Updates a score in the list
def update_score(scores):
  # Print the scores in a numbered list
  for i in range(len(scores)):
    print(f"{i+1}. {scores[i]}")

  # Prompt the user for the score they want to update
  score_to_update = int(input("Enter the number of the score you want to update: "))
  while score_to_update < 1 or score_to_update > len(scores):
    print("Error - score number must be between 1 and the number of scores. Please reenter")
    score_to_update = int(input("Enter the number of the score you want to update: "))
  
  # Prompt the user for the new score
  new_score = int(input("Enter the new score: "))
  while new_score < 0 or new_score > 100:
    print("Error - test score must be between 0 and 100. Please reenter")
    new_score = int(input("Enter a test score: "))
  
  # Update the score
  scores[score_to_update - 1] = new_score

  # Redisplay scores
  display_scores(scores)

# Find scores above and below the average and display them
def mine_scores(scores):
  # calculate the average(again...)
  total = 0
  for score in scores:
    total += score

  average = total / len(scores)

  # use list comprehension to find scores greater than or equal to the average, including the average itself
  high_scores = [score for score in scores if score >= average]

  # use list comprehension to find scores less than the average
  low_scores = [score for score in scores if score < average]

  # Sort each list in ascending order
  high_scores.sort()
  low_scores.sort()

  print ("High scores: ")
  for score in high_scores:
    print(f"{score:>20,.2f}")

  print ("Low scores: ")
  for score in low_scores:
    print(f"{score:>20,.2f}")

# Find the max, min, and average of the scores and display them
def score_metrics(scores):
  # gather highest and lowest scores, get a sum for later average while we're at it
  max = 0
  min = 0
  total = 0
  for score in scores:
    if score > max:
      max = score
    if score < min:
      min = score
    total += score
  
  # Calculate the average
  average = total / len(scores)

  # Print metrics
  print (f"Max score: {max:>20,.2f}")
  print (f"Min score: {min:>20,.2f}")
  print (f"Average score: {average:>16,.2f}")

# Gathers the number of scores
def input_scores():
  scores = []

  # Gather the number of scores the user wants to enter
  num_tests = int(input("Enter the number of test scores to enter: "))
  while num_tests <= 0:
    print("Error - number of tests must be greater than zero. Please reenter")
    num_tests = int(input("Enter the number of test scores to enter: "))
  
  # Gather the actual scores specified by the user
  for score in range(num_tests):
    score = int(input("Enter a test score: "))
    while score < 0 or score > 100:
      print("Error - test score must be between 0 and 100. Please reenter")
      score = int(input("Enter a test score: "))
    scores.append(score)

  return scores

# Displays the menu
def display_menu():
  print("""
  1. Process Scores (min/max/average)
  2. Mine Scores (low/high scores)
  3. Update Score
  4. Display Scores
  5. Quit
  """)

# Program entrypoint
main()