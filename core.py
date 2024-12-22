from sys import exit

def check_input(prompt):
    while True:
        temp = input(prompt)

        if temp == "y":
            return True
        elif temp == "n":
            return False
        else:
            print('Invalid input. Please try again.')

def exit_message():
    print('Alright. Thanks for trying football manager.')
    exit()
