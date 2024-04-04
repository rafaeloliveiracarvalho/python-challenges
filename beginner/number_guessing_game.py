import random


def game():
    lower_limit = int(input("Type the lower limite of range (integer): "))
    upper_limit = int(input("Type the upper limit of range (integer): "))

    print(f"Try guess a number of {lower_limit} to {upper_limit}")

    random_num = random.randint(lower_limit, upper_limit)

    end_game = False

    while not end_game:
        guess = int(input("What's your guess?\n"))

        if guess > random_num:
            print("Upper Guess!! Try again.")
        elif guess < random_num:
            print("Lower Guess!! Try again.")
        else:
            print("You Won!!")
            end_game = guess == random_num

    play_again = input("Play again? (Y/n): ")

    if play_again in ["", "Y", "y"]:
        game()
    else:
        print("End Game!!")


if __name__ == "__main__":
    game()

# Future Features
# 1 - Integer validation
# 2 - Ensure that lower limit is less than upper limits
# 3 - Tries limit 3
