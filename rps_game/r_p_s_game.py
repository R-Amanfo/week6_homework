import random     # Import the random module to generate random numbers
from emoji import emojize

# defining the function
def get_user_choice() :
    """ This function prompts the user to enter their choice of Rock, Paper, or Scissors.
    :return: str Represents the user's choice as a string, either "Rock", "Paper", or "Scissors"."""
      # Dictionary to map user input
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors','L':'Lizard','SP':'Spock'}
    while True:      # Infinite loop that keeps running until the user enters a valid input
        user_input = input("Enter your choice (R = Rock, P = Paper, S = Scissors, L = Lizard, SP = Spock):\n").upper()
        if user_input in choices:      # user_input = 'R'
            user_response = choices[user_input]  # choices[R] is 'Rock', because 'R' maps to 'Rock' in choices.
            return user_response      # This returns the valid choice, e.g., "Rock"
        else:
            print("Invalid choice! Please enter R, P, S, L, or SP.") # Ask again if input is invalid
            #return get_user_choice()      # This calls the function again to ask the user for input again
    # The return statement returns an object of the type based on the expression's

def get_computer_choice():
    """This function randomly selects a choice for the computer: Rock, Paper, or Scissors.
     :return: str Represents the computer's choice as a string, either "Rock", "Paper", or "Scissors"."""
    choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3:'Lizard', 4:'Spock'}  # Dictionary to map numbers to choices
    random_number = random.randint(0, 4)  # Generate a random number between 0 and 2
    comp_response = choices[random_number]
    return comp_response  # Return the value back to the user

def determine_winner(user, computer):
    """This function compares the user's and computer's choices to determine the winner.
     :param1 user: str Represents the user's choice ("Rock", "Paper", or "Scissors").
     :param2 computer: str Represents the computer's choice ("Rock", "Paper", or "Scissors").
     :return: str The result of the game ("You win!", "You lose!", or "It's a draw!")."""
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

    if user == computer:
        return "It's a draw! 🤝 Both chose the same.",None

    elif (user, computer) in winning_cases:
        # Returning 2 values, the result message from the winning_cases dictionary based on user and computer choices
        return f"YOU WIN!! 🎉 {winning_cases[(user, computer)]}" , 'user'

    else:
        return f"YOU LOSE! 😢 {winning_cases[(computer, user)]}", 'computer'


def play_game(rounds=3):
    ####### Main function ########
    """The main entry point of the program where the game logic is executed.
    Plays a complete game of Rock, Paper, Scissors between the user and the computer.
    :return: None This function does not return any value."""
    print("*" * 80)
    user_score = 0
    computer_score = 0
    total_rounds = 0

    while total_rounds < rounds:

        print("~~~ Welcome to Rock, Paper, Scissors, Lizard, Spock Game! ~~~")
        user_choice= get_user_choice()
        comp_choice = get_computer_choice()

        print(f"\nThe user choice is : {user_choice}")      # Display user choice
        print(f"The Computer choice is : {comp_choice}")  # Display computer choice
        print("~" * 50)

        result , winner = determine_winner(user_choice,comp_choice)  # Determine the winner,there are two variables so need to return two values
        print(f"The result is : {result} ")
        #print(winner)
        print("*" * 50)
        if winner == 'user':
            user_score +=1
        elif winner == 'computer':
            computer_score +=1
        else:
            user_score +=1
            computer_score +=1

        total_rounds += 1
        print(f"\nYour score is : {user_score}  |  Computer score is : {computer_score}")
        print("\n" + "*" * 50)

    # Display final winner based on the score
    if user_score > computer_score:
        print(f"{emojize(':party_popper:')} Congratulations, You won!! \U0001F600")
    elif user_score < computer_score:
        print(f"{emojize(':desktop_computer:')} Computer Wins! Try again!! \U0001F642")
    else:
        print("It's tie overall!\U0001F642")



# This block will only run when rock_paper_scissors.py is executed directly,not when imported.
# It prevents the game logic from running automatically when the script is imported into another program.
if __name__ == "__main__":
    play_game()


