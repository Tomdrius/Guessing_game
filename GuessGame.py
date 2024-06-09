# This is a guess game from 1 to 30.
import random

UPPER_BORDER_NUMBER = 30
in_scale_text = " and not in the scale"

print("Tell me Your name. I want to know who I talk to.")
user_name = input()
print("Hi, " + user_name)

searched_number = random.randint(1, UPPER_BORDER_NUMBER)
print(f"Guess a number between 1 and {UPPER_BORDER_NUMBER}. I will help You a little")

for attempt_number in range(1, 9):
    print("Take a guess")
    try:
        guess_number = int(input())
        in_scale = 1 <= guess_number <= UPPER_BORDER_NUMBER
        if guess_number < searched_number:
            low_message = "Your number is too low" + (in_scale_text if not in_scale else "")
            print(low_message)
        elif guess_number > searched_number:
            high_message = "Your number is too big" + (in_scale_text if not in_scale else "")
            print(high_message)
        else:
            break
    except ValueError:
        print("You are guessing a number, not the meaning of life")

if guess_number == searched_number:
    win_message = "You found the correct number in " + str(attempt_number) + " attempts, congratulation"
    print(win_message)
else:
    fail_message = "The correct number was " + str(searched_number)
    print(fail_message)
