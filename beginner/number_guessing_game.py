import random


def game(lower_limit=None, upper_limit=None, random_num=None, guess=None):
    lower_limit = (
        int(input("Type the lower limite of range (integer): "))
        if not lower_limit
        else lower_limit
    )

    upper_limit = (
        int(input("Type the upper limit of range (integer): "))
        if not upper_limit
        else upper_limit
    )

    print(f"Try guess a number of {lower_limit} to {upper_limit}")

    random_num = (
        random.randint(lower_limit, upper_limit) if not random_num else random_num
    )

    guess = int(input("What's your guess?\n")) if not guess else guess

    if guess > random_num:
        print("Upper Guess!! Try again.")
        game(
            lower_limit=lower_limit,
            upper_limit=upper_limit,
            random_num=random_num,
        )

    elif guess < random_num:
        print("Upper Guess!! Try again.")
        game(
            lower_limit=lower_limit,
            upper_limit=upper_limit,
            random_num=random_num,
        )

    else:
        print("You Won!!")

    jogar_novamente = input("Play again? (Y/n): ")
    if jogar_novamente in ["", "Y", "y"]:
        game()

    print("End Game!!")


if __name__ == "__main__":
    game()

# Future Features
# 1 - Integer validation
# 2 - Ensure that lower limit is less than upper limits
