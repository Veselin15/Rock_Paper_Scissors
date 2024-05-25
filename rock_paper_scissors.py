import random
class colors:

    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'


    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
        white = '\033[97m'''


    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
score = 0

def play_game():
    global score

    print(colors.fg.white, "Choose [r]ock, [p]aper, [s]cissors:", end = " ")
    player_move = input()

    if player_move.lower() == "r":
        player_move = rock
    elif player_move.lower() == "p":
        player_move = paper
    elif player_move.lower() == "s":
        player_move = scissors
    else:
        raise SystemExit(colors.fg.red, "Invalid Input for player's move. Try again...")

    computer_random_move = random.randint(1,3)

    if computer_random_move == 1:
        computer_move = rock
    elif computer_random_move == 2:
        computer_move = paper
    elif computer_random_move == 3:
        computer_move = scissors

    print(colors.fg.blue, f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        score += 1
        print(colors.fg.green, f"You win! Your score is: {colors.fg.yellow}{score}.")


    elif (player_move == scissors and computer_move == rock) or \
            (player_move == rock and computer_move == paper) or \
            (player_move == paper and computer_move == scissors):
        print(colors.fg.red, f"You lose! Computer wins! Your score is: {colors.fg.yellow}{score}.")

    else:
        print(colors.fg.blue, f"It's a draw! Your score is: {colors.fg.yellow}{score}.")

    restart = input("Do you want to play again? [yes]/ [no]: ")
    if restart.lower() == 'yes':
        play_game()
    else:
        print(colors.fg.blue, f"Your final score is: {colors.fg.yellow}{score}.")
        print(colors.fg.green, "Thank you for playing!")

play_game()