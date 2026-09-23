# How it works

The whole program is in one Python file. When I run it, Python reads the file from the top and creates the functions, but nothing on screen happens until the last line, which is `main()`. `main()` shows the menu and keeps going until I choose quit.

This is the rough path through the program:

```text
start
  |
  v
main() keeps looping
  |
  +-- 1 --> run_caesar() --> encrypt()
  |
  +-- 2 --> guessing_game() --> rounds() --> encrypt()
  |
  +-- 0 --> prints Goodbye and stops
  |
  +-- anything else --> prints Invalid Choice and shows the menu again
```

## The menu

I split this into two functions because printing the menu and reading the choice are different jobs.

`menu()` only prints the box. It does not ask for input.

`main()` is a `while True` loop, so it repeats until I tell it to stop. Each time around it does this:

1. Call `menu()` so the box is printed.
2. Use `input()` to read what the user typed, then `.strip()` to remove spaces at the ends.
3. If they typed `"1"`, call `run_caesar()`.
4. If they typed `"2"`, call `guessing_game()`.
5. If they typed `"0"`, print `Goodbye!` and `break`. That leaves the loop, so the program ends.
6. If they typed anything else, print `Invalid Choice`. The loop just starts again, so the menu comes back.

Choosing `1` or `2` does not quit. When that function finishes, Python comes back to `main()` and the menu is printed again.

## The Caesar cypher

`encrypt(message, shift)` goes through the message one character at a time and builds a new string called `encrypted`.

For each character I check `char.isalpha()`:

- If it is not a letter, I add it to the result unchanged. So spaces, numbers and punctuation stay where they are. `Hello, world!` with a shift of 3 becomes `Khoor, zruog!`. The comma, the space and the `!` do not move.
- If it is a letter, I need to know if it is uppercase or lowercase, because `A` and `a` are different character codes. Uppercase starts at `65` (`A`). Lowercase starts at `97` (`a`). I store that in `base`.

Then the actual shift is this line:

```python
chr((ord(char) - base + shift) % 26 + base)
```

What that does, in order:

1. `ord(char)` turns the letter into its number. `a` is `97`.
2. I subtract `base`, so `a` becomes `0` and `b` becomes `1`. That makes the alphabet easier to work with.
3. I add the shift. A shift of 1 turns `0` into `1`.
4. `% 26` wraps it around. There are only 26 letters, so if the number goes past 25 it starts again at 0. That is why `z` with a shift of 1 becomes `a`, and `Z` becomes `A`.
5. I add `base` back so it is a real character code again, and `chr` turns that number back into a letter.

Uppercase and lowercase are done separately, so `Hello` with a shift of 1 becomes `Ifmmp`, not `ifmmp`.

A positive shift moves forward. `a` with a shift of 1 is `b`. A negative whole number moves backward. Python's `%` still gives a number from 0 to 25, so `a` with a shift of `-1` wraps around to `z`.

`run_caesar()` is what option 1 actually does:

1. It asks for the message and stores it as text. If you press Enter without typing anything, the encrypted result is just empty as well.
2. It asks for the shift and uses `int()` to turn the text into a number. `int()` only accepts a whole number. If the user types `three`, nothing, or `1.5`, Python raises a `ValueError`. I do not catch that error, so the program stops. That is a bug I know about.
3. It calls `encrypt` and prints the original message, then the encrypted one.
4. It asks if you want to know how it works. I check `HowItWorks.lower() == "y"`, so only `y` or `Y` prints the explanation. The explanation is only the simple example of 1 shift (`a -> b`). It does not use the shift the user just typed. After that the function ends and the menu comes back.

This version only encrypts. I did not add a decrypt option. Decrypting would be the same function with the shift going the other way. A shift of 3 is undone by a shift of `-3`. A shift of `23` does the same thing, because 26 - 3 = 23.

## The guessing game

The words are stored in a normal list:

`the`, `words`, `are`, `super`, `hard`, `to`, `guess`, `caesar`, `is`, `fun`

It is a small fixed list. I do not load a dictionary from a file.

`guessing_game()` is the outside loop. It calls `rounds()` once, then asks `Would you like to play again? (y/n):`. I use `.lower()`, so only `y` starts another round. Any other answer prints `Thanks for playing! Goodbye!` and the function ends. That sends the user back to the main menu. It does not close the program.

`rounds()` is one go at the game:

1. `random.choice(words)` picks a word. I do not remove it from the list, so the same word can come up again later.
2. `random.randint(1, 25)` picks the shift. I start at 1 so the word always changes. I stop at 25 because a shift of 26 would look exactly the same as the original word, which would make the game pointless. A shift of 0 would do the same.
3. I call `encrypt` to make the puzzle.
4. Then I ask if they are ready. I pick the word and the shift before that question. If they do not type `y` or `Y`, I print `Maybe next time!` and `return`. The puzzle is just thrown away. `guessing_game()` still asks if they want to play again.
5. If they are ready, I print the encrypted word. I do not print the shift. That is what they are trying to work out.
6. I set `attempts` to 3 and use a `while attempts > 0` loop.
   - The guess is turned to lowercase with `.lower()` before I compare it.
   - If it matches the secret word, I print `Correct!` and `return`. That leaves the function straight away, so any guesses they had left are not used.
   - If it does not match, I print `Incorrect` and take 1 off `attempts`. A blank guess counts as wrong. Extra spaces also count as wrong, because I do not use `.strip()` on the guess.
7. When `attempts` hits 0 the loop stops. I print the real word and the shift so they can see the answer.

All of my words are already lowercase. The guess is lowercased before the check, so `Caesar` becomes `caesar` and that matches. The guess still has to be the whole word and nothing else.

## What each function does

- `menu` prints the boxed menu.
- `main` reads the choice and calls the right function until the user quits.
- `encrypt` shifts the letters and leaves everything else alone.
- `run_caesar` asks for the message and the shift, prints the result, and can show the short explanation.
- `rounds` is one round: a random word, a random shift, and 3 guesses.
- `guessing_game` keeps playing rounds until the user says they do not want another one.

## Things this version still does not do

- If the shift is not a whole number, option 1 crashes.
- There is no button or menu option to decrypt.
- The game only has the 10 words in the list.
- A guess has to match the word exactly once it has been lowercased. Extra spaces or punctuation are wrong.
- The "how it works" message always talks about a shift of 1. It does not explain the shift the user actually used.
