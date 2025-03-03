import random     # Import the random module to generate random numbers
from emoji import emojize
# imports the emojize function which allows emojis to be used

# defining the function
def get_user_choice() :
    """ This function prompts the user to enter their choice of Rock, Paper, or Scissors.
    :return: str Represents the user's choice as a string, either "Rock", "Paper", or "Scissors"."""
      # Dictionary maps user input (R,P,S, L & SP to corresponding choices
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors','L':'Lizard','SP':'Spock'}
    while True:      # Infinite loop that keeps running until the user enters a valid input
        # user input this prompts user to enter choice, upper converts it to upper case to match the choice dictionary
        user_input = input("Enter your choice (R = Rock, P = Paper, S = Scissors, L = Lizard, SP = Spock):\n").upper()
        # this checks if the user_input is a valid key in the choices dictionary
        # if its valid it assigns it to the matching value to user_response
        if user_input in choices:      # user_input = 'R'
            user_response = choices[user_input]  # choices[R] is 'Rock', because 'R' maps to 'Rock' in choices.
            return user_response      # This returns the valid choice, e.g., "Rock"
        # else if the input is not valid it prompts user to enter choice again
        else:
            print("Invalid choice! Please enter R, P, S, L, or SP.") # Ask again if input is invalid
            #return get_user_choice()      # This calls the function again to ask the user for input again
    # The return statement returns an object of the type based on the expression's

def get_computer_choice():
    """This function randomly selects a choice for the computer: Rock, Paper, or Scissors.
     :return: str Represents the computer's choice as a string, either "Rock", "Paper", or "Scissors"."""
    choices = {0: 'Rock', 1: 'Paper', 2: 'Scissors', 3:'Lizard', 4:'Spock'}
    # choices variable stores a dictionary, each number maps to Rock, Paper etc
    random_number = random.randint(0, 4)  # Generate a random number between 0 and 2.
    # it is stored in the variable random_number
    # comp_response variable stores the result of the random dictionary look up
    comp_response = choices[random_number]
    # this return statement is used to send back a value to the function
    return comp_response

def determine_winner(user, computer):
    """This function compares the user's and computer's choices to determine the winner.
     :param1 user: str Represents the user's choice ("Rock", "Paper", or "Scissors").
     :param2 computer: str Represents the computer's choice ("Rock", "Paper", or "Scissors").
     :return: str The result of the game ("You win!", "You lose!", or "It's a draw!")."""
    # it's a dictionary and Each key is a tuple of (user_choice, computer_choice),& the value is the reason why the user wins.
    # eg paper wins over rock
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
    # this statement is checking if the user and comp entry is the same so its a draw (a message)
    # second value None to indicate no winner
    if user == computer:
        return "It's a draw! 🤝 Both chose the same.",None
    # checking if user wins None = null
    # checks if this combination is in the winning cases dictionary above
    # if it does it posts message user wins
    # second value user to indicate user is in the winner
    elif (user, computer) in winning_cases:
        # Returning 2 values, the result message from the winning_cases dictionary based on user and computer choices
        return f"YOU WIN!! 🎉 {winning_cases[(user, computer)]}" , 'user'
    # if none of the above conditions are met then computer wins
    # the function looks up the computer, user in the winning dictionary to explain why it won
    # function then returns You lose and second value 'computer' as computer is the winner in this case
    else:
        return f"YOU LOSE! 😢 {winning_cases[(computer, user)]}", 'computer'

# define function
# has a parameter 'rounds', default value of 3
# has 3 rounds unless specified otherwise
def play_game(rounds=3):
    ####### Main function ########
    """The main entry point of the program where the game logic is executed.
    Plays a complete game of Rock, Paper, Scissors between the user and the computer.
    :return: None This function does not return any value."""
    print("*" * 80)
    # variables keep track of the score
    # set to 0
    user_score = 0
    computer_score = 0
    total_rounds = 0

    # while loop for rounds
    # ensures game is run for the specified number of rounds
    # it runs as long as total_rounds is less than rounds
    while total_rounds < rounds:
        # prints welcome message at start of each round
        print("~~~ Welcome to Rock, Paper, Scissors, Lizard, Spock Game! ~~~")
        # functions to call the user choice & computer choice
        user_choice= get_user_choice()
        comp_choice = get_computer_choice()
        # displays the choices for this round
        print(f"\nThe user choice is : {user_choice}")      # Display user choice
        print(f"The Computer choice is : {comp_choice}")  # Display computer choice
        print("~" * 50)
        # calls function to determine winner. returns a results message
        result , winner = determine_winner(user_choice,comp_choice)
        # Determine the winner,there are two variables so need to return two values
        print(f"The result is : {result} ")
        #print(winner)
        print("*" * 50)
        # updates score
        # if block if user wins the round their score is incremented by 1
        # if computer wins their score is incremented by `
        # if its  a draw both incremented by 1
        if winner == 'user':
            user_score +=1
        elif winner == 'computer':
            computer_score +=1
        else:
            user_score +=1
            computer_score +=1
        # this increase the total rounds counter by 1 after each round is played
        total_rounds += 1
        print(f"\nYour score is : {user_score}  |  Computer score is : {computer_score}")
        print("\n" + "*" * 50)

    # Display final winner based on the score
    # after the while loop compares the choices of user and computer
    # message displayed with emoji depending on result
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
