import random
# section 1 - main menu
def main():
    while True:
        menu()

        choice = input("select an option")
        if choice == "1 -- caesar cypher":
            run_caesar()
        elif choice == "2 -- caesar cypher game":
            guessing_game()
        elif choice == "0":
            break

        else:
            print("Invalid Choice")

# Section 2 
# Caesar cypher
def run_caesar():

    print("Enter your message to be encrypted below")
    message1 = input("Enter message: ")
    shift = int(input("Enter shift (num) :"))
    encrypted1 = encrypt(message1, shift)
    print("message1")
    print("encrypted1")
    HowItWorks = input("Would you like to know how it works? (y/n): ")
    if HowItWorks == "y" :
                print("The cypher rotates the letters based on the shift made, for example 1 shift would look like (a -> b)")
# custom cypher

words = ["the","words","are","super","hard","to","guess","caesar","is","fun"]
select_word = random.choice(words)
shift_amount = random.randint(1, 25)
encrypted_word = ""

for characters in select_word:
    if char.isalpha():
        encrypted_word += chr((ord(char) + shift_ammount - 97) %26 + 97)
        else:
            encrypted_word +- char
    
def guessing_game():

    choice = input("are you ready to play (y/n)")
    if choice == "y":
        print("This game will have a randomly shifted caesar cypher)
        print("Your job is to find out the word
        print("You have 3 attempts -- GOOD LUCK")
        
        


    



   
    

    
    
