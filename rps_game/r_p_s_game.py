#import random     # Import the random module to generate random numbers
from emoji import emojize  # from emoji module importing emojize function
from random import *    # from random module importing all functions

# defining the function
def get_user_choice() :
    """ This function prompts the user to enter their choice of Rock, Paper,Scissors,Lizard or Spock.
    :return: str Represents the user's choice as a string, either "Rock", "Paper","Scissors","Lizard","Spock"."""
      # Dictionary to map user input
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors','L':'Lizard','SP':'Spock'}
    while True:      # A loop control statement that keeps running as long as the condition is True.
        user_input = input("Enter your choice (R = Rock, P = Paper, S = Scissors, L = Lizard, SP = Spock):\n").upper()
        if user_input in choices:      # user_input = 'R'
            user_response = choices[user_input]  # choices[R] is 'Rock', because 'R' maps to 'Rock' in choices.
            return user_response      # This returns the valid choice, e.g., "Rock" and exit the function
        else:
            print("Invalid choice! Please enter R, P, S, L, or SP.") # Ask again if input is invalid
            # The return statement returns an object of the type based on the expression's

def get_computer_choice():
    """This function randomly selects a choice for the computer: Rock, Paper,Scissors,Lizard or Spock.
     :return: str Represents the computer's choice as a string, either "Rock", "Paper","Scissors","Lizard","Spock"."""
    choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3:'Lizard', 4:'Spock'}  # Dictionary to map numbers to choices
    random_number = randint(0,4)  # Generate a random number between 0 and 2
    comp_response = choices[random_number]
    return comp_response  # Return the value back to the user
    # choices = ['Rock','Paper','Scissors','Lizard','Spock'] # list of choices,randomly selects choice
    # return choice(choices)

def determine_winner(user, computer):
    """This function compares the user's and computer's choices to determine the winner.
     :param1 user: str Represents the user's choice ("Rock", "Paper","Scissors","Lizard","Spock").
     :param2 computer: str Represents the computer's choice ("Rock", "Paper","Scissors","Lizard","Spock").
     :return: tuple (str, str) The result of the game and the winner.
            The first value is a string with the result message.
            The second value is a string indicating the winner: 'user', 'computer', or None for a draw."""
    # it's a dict and Each key is a tuple of (user_choice, computer_choice),& the value is the reason why the user wins.
    winning_cases = {
        ("Rock", "Scissors"): "Rock crushes Scissors!",
        ("Rock", "Lizard"): "Rock crushes Lizard!",
        ("Paper", "Rock"): "Paper covers Rock!",
        ("Paper", "Spock"): "Paper disproves Spock!",
        ("Scissors", "Paper"): "Scissors cuts Paper!",
        ("Scissors", "Lizard"): "Scissors decapitates Lizard!",
        ("Lizard", "Spock"): "Lizard poisons Spock!",
        ("Lizard", "Paper"): "Lizard eats Paper!",
        ("Spock", "Scissors"): "Spock smashes Scissors!",
        ("Spock", "Rock"): "Spock vaporizes Rock!",
    }
     # comparing user and computer value
    if user == computer:
        return f"It's a draw! {emojize(':handshake:')} Both chose the same.", None   # 🤝 Handshake,None is a keyword that represents the absence of a value
    # This is checking whether the tuple (user, computer) exists as a key in the winning_cases dictionary.
    elif (user, computer) in winning_cases:
        return f"YOU WIN!! {emojize(':party_popper:')} {winning_cases[(user, computer)]}", 'user'  # accessing the value associated with the key tuple (user, computer) in the dictionary.🎉 Party Popper
    else:
        return f"YOU LOSE! {emojize(':crying_face:')} {winning_cases[(computer, user)]}", 'computer'  # 😢 Crying Face


def play_game(rounds=3):
    ####### Main function ########
    """The main entry point of the program where the game logic is executed.
    This function runs multiple rounds (default is 3) where the user and computer
    make their choices, the winner is determined, and scores are tracked.
    The final winner is declared based on the highest score.
    :return: None This function does not return any value."""
    print("*" * 80)
    # Initialize user and computer scores to 0 at the start of the game
    user_score = 0
    computer_score = 0
    # Initialize the total rounds count to 0, to keep track of how many rounds have been completed
    total_rounds = 0  # Counts the total number of rounds played

    # As long as this condition is True,the loop will continue to execute.Once total_rounds is equal to or greater than rounds, the loop will stop.
    while total_rounds < rounds:

        print("\n~~~ Welcome to Rock, Paper, Scissors, Lizard, Spock Game! ~~~")
        user_choice= get_user_choice()   # Call the function to get user's choice
        comp_choice = get_computer_choice()  # call the function to get the computer's random choice

        print(f"\nThe user choice is : {user_choice}")      # Display user choice
        print(f"The Computer choice is : {comp_choice}")  # Display computer choice
        print("~" * 70)

        # result: This will hold the message string, like "YOU WIN!! 🎉 Rock crushes Scissors!"
        # winner: This will hold 'user' or 'computer', depending on who won.
        result , winner = determine_winner(user_choice,comp_choice) #call the function and returns 2 values
        print(f"Round {total_rounds + 1} result is : {result} ")  # prints the number of rounds and the result of that round.
        print(f"So,the winner of Round {total_rounds + 1} is : {winner}")
        print("~" * 70)
        # Update scores based on who won
        if winner == 'user':     # if this condition is true the user score will be incremented by 1
            user_score +=1
        elif winner == 'computer':
            computer_score +=1        # the computer score will be incremented by 1
        else:
            # Tie case (you can choose to give points for ties or not)
            print("It's a tie! Both get a point.")
            user_score +=1      # executes when the user and computer is tie, both gets a point
            computer_score +=1

        total_rounds += 1   # # Increment the round count after each round
        print(f"SCORES : YOUR SCORE is : {user_score}     |     COMPUTER SCORE is : {computer_score}")
        print(f"Completed {total_rounds} rounds")
        print("-" * 70)

    # Final result printing after all rounds
    print ("*********************** FINAL RESULT *************************** ")

    # Display Final Winner based on the score
    if user_score > computer_score:
        print(f"Final Score: USER SCORE = {user_score}  |  COMPUTER SCORE = {computer_score}")
        print(f"The final result of the rounds is : {emojize(':party_popper:')} Congratulations, You are the winner!! \U0001F600")
    elif user_score < computer_score:
        print(f"Final Score: USER SCORE = {user_score}  |  COMPUTER SCORE = {computer_score}")
        print(f"The final result of the rounds is : {emojize(':desktop_computer:')} Computer Wins! Try again next time!! \U0001F642") # unicode for smiley emoji
    else:
        print(f"Final Score: USER SCORE = {user_score}  |  COMPUTER SCORE = {computer_score}")
        print("It's tie! Well played by both!\U0001F642")


    print("GAME OVER!!!!")

# This block will only run when rock_paper_scissors.py is executed directly,not when imported.
# It prevents the game logic from running automatically when the script is imported into another program.
if __name__ == "__main__":
    play_game()  # can change the number of rounds here
#play_game()

