
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random  # Import the random module

game_images = [rock, paper, scissors]  # Example images (Replace with actual ASCII images)

while True:  # Infinite loop to keep playing
    user_input = input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or 'exit' to quit: ")

    if user_input.lower() == "exit":
        print("Thanks for playing! Goodbye!")
        break  # Exit the loop

    if not user_input.isdigit():  # Check if input is not a number
        print("Invalid input! Please enter a number between 0 and 2.")
        continue  # Ask again

    user_choice = int(user_input)

    if user_choice < 0 or user_choice > 2:  # Check for valid range
        print("Invalid choice! Please choose 0, 1, or 2.")
        continue  # Ask again

    print(f"You chose: {game_images[user_choice]}")  # Show user choice

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_images[computer_choice]}")  # Show computer choice

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
