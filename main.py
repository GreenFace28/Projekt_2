"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Michal Vlach
email: mvlach@seznam.cz
"""
# import knihovny
import random

# pomocné proměnné
separator = "-" * 47

# funkce pro průběh hry
def welcome():
    """ Funkce pro uvítání uživatele """
    print("Hi there!")
    print(separator)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)
    print("Enter a number:")
    print(separator)

def generate_number():
    """ Funkce pro vygenerování náhodného 4místného čísla """
    number = "2017"  # random.sample(range(1, 9), 4)
    return "".join(map(str, number))

def user_input():
    """ Funkce pro získání vstupu od uživatele """
    while True:
        user_number = input(">>> ")
        if len(user_number) == 4 and user_number.isdigit():
            return user_number
        else:
            print("Please enter a valid 4-digit number.")
            print(separator)

def check_bulls(number, user_number):
    """ Funkce pro kontrolu počtu bulls """
    bulls = sum(1 for n, u in zip(number, user_number) if n == u)
    return bulls

def check_plural_bulls(num_bulls):
    """ Funkce pro kontrolu množného čísla u bulls """
    if num_bulls == 1:
        bull = "bull"
    else:
        bull = "bulls"
    return bull

def check_cows(number, user_number):
    """ Funkce pro kontrolu počtu cows """
    cows = sum(1 for n in user_number if n in number) - check_bulls(number, user_number)
    return cows

def check_plural_cows(num_cows):
    """ Funkce pro kontrolu množného čísla u cows """
    if num_cows == 1:
        cow = "cow"
    else:
        cow = "cows"
    return cow

def guess_count():
    """ Funkce pro počítání počtu pokusů """
    if 'guess' not in globals():
        global guess
        guess = 0
    guess += 1
    return guess

def check_game(bulls):
    """ Funkce pro kontrolu ukončení hry """
    if bulls == 4:
        return True
    else:
        return False   

# Funkce pro spouštění hry
def main():
    """ Hlavní funkce pro spuštění hry """
    welcome()
    number = generate_number()

    while True:

        bulls = check_bulls(number, user_number)
        cows = check_cows(number, user_number)
        guess = guess_count()
        print(f"{bulls} {check_plural_bulls(bulls)}, {cows} {check_plural_cows(cows)}")
        
        if check_game(bulls):
            print(f"Correct, you've guessed the right number in {guess} guesses!")
            print(separator)
            print("That's amazing!")
            break

if __name__ == "__main__":
    main()
