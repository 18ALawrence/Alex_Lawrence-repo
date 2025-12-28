import random

current_number = random.randint(1, 100)
score = 0
game_over = False

print("Welcome to Higher or Lower!")
user_name = input("Enter your name: ")

while game_over == False:
    user_guess = input(f"Is the next number going to be higher or lower than {current_number}?")
    next_number = random.randint(1, 100)
    print(f"Your next number is {next_number}")

    if user_guess in ["h", "H", "Higher", "higher"] and next_number > current_number:
        print("Correct, the next number is higher than the current one")
        score = score + 1
        current_number = next_number

    elif user_guess in ["l", "L", "Lower", "lower"] and next_number < current_number:
        print("Correct, the next number is lower than the current one")
        score = score + 1
        current_number = next_number

    else:

        leaderboard_dict = {}

        try:
            with open("leaderboard.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 2:
                        leaderboard_dict[parts[0]] = int(parts[1])

        except FileNotFoundError:
            pass

        print("Unlucky, you were incorrect")
        print(f"Your score is, {score}")

        previous_best = leaderboard_dict.get(user_name, 0)

        if score > previous_best:
            print(f"New High Score, congratulations you beat your old score of {previous_best}")
            leaderboard_dict[user_name] = score

        else:
            print(f"Nice try, your best score is {previous_best}")

        with open("leaderboard.txt", "w") as file:
            for name, saved_score in leaderboard_dict.items():
                file.write(f"{name}, {saved_score}\n")

        play_again = input("Do you want to play again?")

        if play_again in ["y", "Y", "yes", "Yes"]:
            score = 0
            current_number = random.randint(1, 100)
        else:
            game_over = True






