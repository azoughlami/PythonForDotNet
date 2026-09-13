import random


def main():
    show_headers()

    the_number = random.randint(a=1, b=100)

    count = 0
    while True:
        guess = get_guess()
        if not guess:
            continue

        count += 1
        if evaluate_guess(guess, the_number):
            break

    print(f"You got the number in {count} guesses! Thanks")

    return None


def evaluate_guess(guess, number):
    if guess == number:
        print(f"That's it. Iam thinking of  {number}")
    if guess < number:
        print(f"Your guess is too LOW.")
    if guess > number:
            print(f"Your guess is too HIGH.")

    return guess == number


def get_guess():
    try:
        text = input("What number am I thinking of ?")
        val = int(text)

        if val < 1 or 100 < val:
            print(f"{val} is not betwwen 1 and 100")
            return None # null in c#
        return val
    except:
        print(f"{val} is not an integer")
        return None



def show_headers():
    print("-------------------------------------------")
    print("|                                         |")
    print("|           PYTHON HIGH / LOW GAME            |")
    print("|                                         |")
    print("-------------------------------------------")
    print()
    print("I'm thinking of a number between 1 & 100.")
    print("How many steps can you guess it in?")
    print()


if __name__ == "__main__":
    main()
