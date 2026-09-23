# section 1 - main menu
def main():
    while True:
        menu()

        choice = input("select an option")
        if choice == "1":
            run_caesar()
        elif choice == "2":
            run_vigenere()
        elif choice == "3":
            run_enigma()
        elif choice == "4":
            run_modern_encryption()
        elif choice == "5":
            compare_methods()
        elif choice == "6":
            ai_assistant()
        elif choice == "0":
            break

        else:
            print("Invalid Choice")

# Section 2 - Cyphers
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
# vigenere cypher
def run_vigenere():


   
    

    
    
