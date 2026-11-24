import random
print("")
secret_number=random.randint(0,10)
guess_number=int(input("Guess a number between 1 and 10: "))
while guess_number!=secret_number: 
    if secret_number < guess_number:
        guess_number=int(input("Too high! Guess again: "))
    else:
        guess_number=int(input("Too low! guess again: "))

print("congratulation! you guess the number!")


