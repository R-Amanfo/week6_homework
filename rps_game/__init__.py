# __init__.py is a special file that makes a directory a Python Package.
# Without it, Python treats the directory as a regular folder, not a package.
# It allows you to import functions from different modules within the package.

# # cannot directly import modules from the rps_game directory like a package
# import r_p_s_game

# use from and package name followed by . script name or file name then import a function
from rps_game.r_p_s_game import determine_winner
from rps_game.r_p_s_game import get_computer_choice ,get_user_choice

# Get the user and  computer's choice
user_choice= get_user_choice()
computer_choice = get_computer_choice()

# Determine the winner
result, winner = determine_winner(user_choice, computer_choice)

# Print the result
print(result)