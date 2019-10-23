import random

hangman = (
"""
     -----------
     |       |
     |       
     |
     |
     |
     |
     |
     |
     |
     -----------------
""",
"""
     -----------
     |       |
     |       O
     |
     |
     |
     |
     |
     |
     |
     -----------------
""",
"""
     -----------
     |       |
     |       O
     |      -+-
     |
     |
     |
     |
     |
     |
     -----------------
""",
"""
     -----------
     |       |
     |       O
     |      -+-
     |       |
     |
     |
     |
     |
     |
     -----------------
""",
"""
     -----------
     |       |
     |       O
     |      -+-
     |       |
     |      /
     | 
     |
     |
     |
     -----------------
""",
"""
     -----------
     |       |
     |       O
     |      -+-
     |       |
     |      / \\
     | 
     |
     |
     |
     -----------------
""")
MAX_WRONG = len(hangman) -1
word_bank = ("PYTHON","WORDS","SUCKER","SURVIVLE","Superman","POPCORN")

word = random.choice(word_bank)
so_far = "-" * len(word)

wrong = 0
used = []
print("Welcome to Hangman, Good Luck")

while wrong < MAX_WRONG and so_far != word:

     print(hangman[wrong])
     print("\nYou've used the following letters:\n", used)
     print("\nSo far, the word is:\n", so_far)

     guess = input("\n\nEnter your Guess: ")
     guess = guess.upper()

     while guess in used:
          print("You've already guessed that letter", guess)
          guess = input("\n\nEnter your Guess: ")
          guess = guess.upper()

     used.append(guess)
     if guess in word:
          print("\nYes!",guess,"is in the word")
          new = ""
          for i in range(len(word)):
               if guess == word[i]:
                    new += guess
               else:
                    new += so_far[i]
          so_far = new
     else:
          print("\nSorry,",guess,"is not in the word")
          wrong += 1
if wrong == MAX_WRONG:
     print(hangman[wrong])
     print("\nYou've been hanged")
else:
     print("\nyou guessed it")

print("\nThe word was",word)
print("\n\nPress the enter key to exit.")

     


