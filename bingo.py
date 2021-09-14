"""
BINGO!! A game for all ages!

This is a game that draws random numbers from 1 to 90 and displays on screen.
This would avoid a whole lot of cheating that happens in the game! :D
"""

import random
import time
import sys

numbers = list(range(1, 91))
random.shuffle(numbers)


def dot_print(dots, secs):
    """
    Prints dots with an interval of given seconds.
    :param dots: The number of dots to print.
    :param secs: The interval between each dot.
    :return: Prints the dots directly to the screen.
    """
    for i in range(dots):
        time.sleep(secs)
        sys.stdout.write('.')
        sys.stdout.flush()


# GAME STARTS HERE...
print("\n\nStarting the game")
dot_print(3, 0.8)

# Displaying Author info
print("\n" + "******" * 10, "BINGO!!!", "******" * 10 + "\n"
                                                        "Author: Romit Thete\n"
                                                        "Last Revised date: 14-Sep-2021")
print("*****" * 26)

print("\nHope you have a good time. May the best player Win ", end='')
dot_print(2, 1)
print()

# Creating an empty list to record the drawn numbers.
drawn_list = []

# Loop plays the game!
while numbers:
    # Display Menu
    print("\n" + "*" * 30, "Key Mapping", "*" * 30, "\n"
                                                    "Enter\t\t\t\t:\tDraw a new number\n"
                                                    "'s' + Enter\t\t\t:\tDisplay the numbers drawn so far\n"
                                                    "'q' or 'e'+ Enter\t\t:\tExit the game")
    print("*" * 73)
    user_inp = input("Enter your choice:\n")

    # Exit logic
    if user_inp.lower() in ['q', 'e']:
        confirm = input("\n[WARNING!!] This will exit the game!\nTo continue playing, type 'play'.\n"
                        "To exit, press the Enter key or type 'yes'...\n")
        if confirm == '' or confirm in ['yes', 'y', 'q', 'e', 'exit', 'quit']:
            if drawn_list:
                print("Total Numbers drawn out:\n{}\n".format(drawn_list))
            print('Thanks for playing! Have a great day!!')
            break
        else:
            print("\nYou entered '{}'.\nContinuing!!".format(confirm))
            continue

    # Draw a new number from a random list
    elif user_inp == "":
        drawn = numbers.pop()
        drawn_list.append(drawn)
        print(drawn)

    # Display the numbers drawn in a sorted manner
    elif user_inp.lower() == 's':
        print("\nDrawn numbers so far:\n{}".format(sorted(drawn_list)))

    else:
        print("Invalid option!")
        continue

# if all numbers from 1 to 90 have been utilized
if not numbers:
    print('\n\nAll the numbers are drawn out! \nThanks for playing!!')
