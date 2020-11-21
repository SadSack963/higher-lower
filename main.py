import random
import os

from art import logo, vs
from game_data import data


def cls():
    """Cross-platform clear screen"""
    os.system('cls' if os.name=='nt' else 'clear')


def get_text(x):
    """Returns the initial text which is subsequently printed in front of the list item"""
    text_list = ["Compare A", "Against B"]
    return text_list[x]


def print_line(items, y):
    """Requires the list of items, and the item number, which is then printed to the console"""
    text = get_text(y)
    name = items[y]["name"]
    description = items[y]["description"]
    country = items[y]["country"]
    print(f"{text}: {name}, a {description}, from {country}")


def get_choice():
    """Get the choice of A or B from the player, and return 0 or 1 accordingly"""
    answer = ""
    while answer != "a" and answer != "b":
        answer = input("Who has more followers? Type 'A' or 'B' : ").lower()
        # check answer for 'a' or 'b'. If neither then try again
        if answer == "a":
            return 0
        elif answer == "b":
            return 1
        else:
            print("Please answer \"A\" or \"B\"")


def get_answer(items):
    """Compare items and return 0 if A > B, 1 if A < B"""
    if items[0]["follower_count"] > items[1]["follower_count"]:
        return 0
    else:
        return 1


def game():
    items = [0,1]
    score = 0
    end_game = False

    print(logo)

    # get first item
    items[0] = random.choice(data)

    # REPEAT from here ...
    while not end_game:
        # get second item
        items[1] = random.choice(data)
        # make sure they are different!
        while items[0] == items[1]:
            items[1] = random.choice(data)
        
        # print first item
        print_line(items, 0)

        # print vs
        print(vs)

        # print second item
        print_line(items, 1)

        # get user answer
        choice = get_choice()

        # compare item follower_count to get correct answer
        answer = get_answer(items)

        cls()
        print(logo)

        # add 1 to score if correct
        if choice == answer:
            score += 1
            print(f"You're right! Current score: {score}\n")

            # get ready for next question
            items[0] = items[1]

            # REPEAT ...

        else:
            print(f"Sorry, that's wrong. Final score: {score}\n")

            # END
            end_game = True

        # print out actual item values
        print(f"A: {items[0]['name']} has {items[0]['follower_count']} million followers")
        print(f"B: {items[1]['name']} has {items[1]['follower_count']} million followers")
        print("\n\n")



game()