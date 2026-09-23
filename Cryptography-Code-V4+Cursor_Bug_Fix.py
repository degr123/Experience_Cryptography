import random

# section 1 - main menu
def menu():
    print("\n--- Cryptography Menu ---")
    print("1 -- caesar cypher")
    print("2 -- caesar cypher game")
    print("0 -- quit")


def main():
    while True:
        menu()

        choice = input("select an option: ").strip()
        if choice == "1":
            run_caesar()
        elif choice == "2":
            guessing_game()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")


# Section 2
# Caesar cypher
def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted


def run_caesar():
    print("Enter your message to be encrypted below")
    message1 = input("Enter message: ")
    shift = int(input("Enter shift (num) :"))
    encrypted1 = encrypt(message1, shift)
    print(message1)
    print(encrypted1)
    HowItWorks = input("Would you like to know how it works? (y/n): ")
    if HowItWorks.lower() == "y":
        print("The cypher rotates the letters based on the shift made, for example 1 shift would look like (a -> b)")


# Cypher game
words = ["the", "words", "are", "super", "hard", "to", "guess", "caesar", "is", "fun"]


def rounds():
    select_word = random.choice(words)
    shift_amount = random.randint(1, 25)
    encrypted_word = encrypt(select_word, shift_amount)

    choice = input("are you ready to play (y/n): ")
    if choice.lower() != "y":
        print("Maybe next time!")
        return

    print("This game will have a randomly shifted caesar cypher")
    print("Your job is to find out the word")
    print("You have 3 attempts -- GOOD LUCK")
    print(f"\nThe encrypted word is: {encrypted_word}")

    attempts = 3
    while attempts > 0:
        guess = input(f"\nEnter your guess ({attempts} attempts left): ").lower()
        if guess == select_word:
            print("Correct!")
            return
        else:
            print("Incorrect")
            attempts -= 1
    print(f"\n You are out of attempts. The correct word was '{select_word}' shifted {shift_amount} times ")


def guessing_game():
    while True:
        rounds()
        again = input("\nWould you like to play again? (y/n): ").lower()
        if again != "y":
            print("\nThanks for playing! Goodbye!")
            break



main()
