# Question 1

# numbers_index = {
#     "1": "first",
#     "2": "second",
# }
#
# commands_list = {
#     "s": "+",
#     "u": "-",
#     "m": "*",
#     "d": "/",
#     "c": "//",
#     "r": "%",
#     "p": "**",
# }
#
# print("Hello! Welcome to simple calculator")
# def main_menu() -> str:
#     choice = input("Please select an option\n1. Enter your first number\n2. Enter your second number\n3. Enter your command\n4. exit\nyour choice: ")
#     return choice
#
# def get_number(index: str, show_hint: bool = False, hint: str = "Please enter a valid float number") -> float:
#     print(hint) if show_hint else ...
#     return float(input(f"Please enter your {numbers_index[index]} number: "))
#
# def get_command(show_hint: bool = False) -> str:
#     print("Please enter a valid option") if show_hint else ...
#     command = input("Please enter your command (\x1B[4ms\x1B[0mum, s\x1B[4mu\x1B[0mbtraction, "
#           "\x1B[4mm\x1B[0multiplication, \x1B[4md\x1B[0mivision, \x1B[4mc\x1B[0morrect division, "
#           "division \x1B[4mr\x1B[0memainder, \x1B[4mp\x1B[0mower): ")
#     return commands_list[command]
#
# while True:
#     user_choice = main_menu()
#     if user_choice == "1":
#         global first_number
#         try:
#             first_number = get_number("1")
#         except ValueError:
#             first_number = get_number("1", True)
#     elif user_choice == "2":
#         global second_number
#         try:
#             second_number = get_number("2")
#         except ValueError:
#             second_number = get_number("2", True)
#     elif user_choice == "3":
#         global user_command
#         try:
#             user_command = get_command()
#         except KeyError:
#             user_command = get_command(True)
#         if (user_command == "/") and (second_number == 0):
#             try:
#                 second_number = get_number("2", True, "number can't divide by zero, try again")
#             except ValueError:
#                 second_number = get_number("2", True)
#
#     else:
#         print("Leaving calculator, Goodbye!")
#         break
#
#     try:
#         print(eval(f"{first_number} {user_command} {second_number}"))
#     except NameError:
#         pass


# Question 2

import random

true_value = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if true_value == guess:
            print(f"Congratulations, you guessed it!\nnumber is {true_value}")
            break
        else:
            print("low") if true_value > guess else print("large")
    except ValueError:
        print("Please enter a valid integer.")
