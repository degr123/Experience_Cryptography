# Experience_Cryptography

# Part 1 - Idea

I built a program which conducts a Caesar cypher on a word the user has imputed and encodes it based on how many shifts the user inputs. Furthermore there is a small guessing game where the user has to try guess the encoded word which has randomised a selected word from a small list

The initial idea for this program comes from an interest in encryption and a fascination with the great efforts of militaries to decrypt and understand opposing forces messages, such as during WW1 and WW2, where it was vital to do so to ensure the safety of your troops. To represent this, I thought it would be interesting to see the differences between the encryption of then and now and how much it has advanced. However I had to change my plans do to the time constraints which I will explain more of in RESEARCH.md

I felt that many people are not aware of the necessity of encryption and how the development of better technologies have made it more crucial then ever to ensure it cant be decoded by malicious actors. This program is to introduce and expose the user to a basic form of encryption to develop a understanding and interest in it

# Part 2 - How to use 

You need Python 3 installed, and a terminal to type in. To run you can double click [Cryptography-Code-Final] script or run it from the terminal

The menu

The menu asks you to type a number and press Enter.

1 encrypt a message. You type the message and you choose the shift.
2 starts the guessing game.
0 prints "Goodbye!" and the program stops.
If you type anything else it prints "Invalid Choice" and shows the menu again

Option 1, the cypher

1. Type your message and press Enter. Spaces and punctuation are allowed. They stay as they are
2. Type the shift as a whole number and press Enter. For example 3
3. The program prints your message, then the encrypted version underneath
4. It asks Would you like to know how it works? (y/n):
   - Type y if you want the short explanation. After that you go back to the menu
   - Type anything else and you go back to the menu with no explanation

Option 2, the game

1. It asks Are you ready to play (y/n):
   - y starts the round.
   - Anything else prints "Maybe next time!" and then it asks if you want to play again
2. You get one encrypted word and 3 guesses
3. Type the word in lowercase. The words in my list are all lowercase, and the program turns your guess into lowercase before it checks it. So "hello" works. capital letters only works if it becomes the exact word after it is lowercased; for example "HelLO" becomes "hello" which would work
4. If you get it right it prints "Correct!" and the round ends, even if you still had guesses left
5. If you get it wrong 3 times it tells you the word and how many times it was shifted
6. Then it asks Would you like to play again? (y/n):
   - y starts a new round. It picks a new word and a new shift
   - Anything else prints "Thanks for playing! Goodbye!" and sends you back to the main menu

That goodbye is only for the game. To quit the program, choose 0 on the menu


# Part 3 - How it works

Open HOWITWORKS.md which was written by Curser to save time

# Part 4 - Improvements

If I had more time I would focus on adding:
- More encryption methods for example enigma
- I would improve the UI to make it more like an app or web app
- Have a section which would answer any user questions about cryptography with the help of AI
- Use a large database of words for the game
- Fine tune the program so little things like not imputing a whole number wont cause the program to fail

# Part 5 - Features

Menu:
- Menu with boxed text

Cypher:
- Uppercase and lowercase both work
- Optional "how it works" explanation after encrypting your word

Game :
- Random word + random shift (1–25) 
- 3 guesses
- play again

# Part 6 - Known limitations

- Shifts must be a whole number or the program will crash
- If nothing is put in the Enter message or Enter shift prompt the program will crash
- Game words are a small fixed list
- Game guesses are compared in lowercase ( Uppercase is not recognised )

