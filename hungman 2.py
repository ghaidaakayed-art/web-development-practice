#استدعي المكتبه 
import random 
#creat list with the words
word=["good","bad","angry","hangry"]
#computer choise 
random_word=random.choice(word)


#creat list for letter

display=[]

HANGMANPICS = [ '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#add _ insted letter

display=["_"]* len(random_word)

print(" ".join(display))

guessed_letter=[]
print(HANGMANPICS[0])


#used while to guess the letter and ask 
lives=6
while "_" in display and lives > 0:
    guessed=input("please guess a letter: ").lower()

    if guessed in guessed_letter:
        print("you already guessed that! try again. ")
        print(f"you have {lives} more tries")
        continue

    guessed_letter.append(guessed)
    
    if guessed not in random_word:
        lives-=1

    

    for position in range(len(random_word)):
        if random_word[position] == guessed:
            display[position] = guessed

    print(" ".join(display))
    print(f"you have {lives} more tries")
    print(HANGMANPICS[6-lives])
    


if lives == 0 :
    print("""
        ************
        you lose!
        ************
        """)

    print(HANGMANPICS[-1])

else:
    print("""
        ************
        you win! 
        ************
        """)