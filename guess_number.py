import random
import json
import datetime

current_time = datetime.datetime.now()
min = 1
max = 50
secret = random.randint(min, max)
guess = 0
attempts = 0
wrong_guess = 0
player_name = input("Write your name: ")

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())

    sorted_score_list = sorted(score_list, key=lambda i: i['attempts'])[:3]

    for score_dict in sorted_score_list:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("datetime") + ", player name: " + score_dict.get("player name") + ", wrong guesses: " + str(score_dict.get("wrong_guess")))

while True:
    guess = int(input("Guess a secret number (between {0} and {1}): " .format(1,50)))
    attempts += 1
    wrong_guess = attempts - 1

    if guess == secret:
        score_data = {
            "attempts": attempts,
            "datetime": str(current_time),
            "player name": player_name,
            "wrong_guess": wrong_guess,
        }
        score_list.append(score_data)

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("Congratulations!")
        break

    elif guess > secret:
        print("Try again with lower number.")

    elif guess < secret:
        print("Try again with higher number.")

print("You have attemted {0} time(s)" .format(attempts))