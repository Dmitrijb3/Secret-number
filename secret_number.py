import datetime
import json
import random

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list[:3]))

for score_dict in score_list:
    score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. Wrong guesses were {4}".format(score_dict.get("name"),
                                                                                        str(score_dict.get("attempts")),
                                                                                        score_dict.get("date"),
                                                                                        str(score_dict.get("secret")),
                                                                                        str(score_dict.get("wrong_guess")))
    print(score_text)
wrong_guess = []
name = input("Please enter your name: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"Player name": name, "attempts": attempts, "date": str(datetime.datetime.now()), "secret_number": secret, "wrong_guess": wrong_guess})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong_guess.append(guess)