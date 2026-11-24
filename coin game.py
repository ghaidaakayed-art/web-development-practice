import random 
print("Welcome to the coin Guessing game!")
print("Choose a method to toss the coin:")
print("1. using random.random()")
print("2. using random.randint()")
input_method = int(input("Enter your choice (1 or 2): "))
if input_method == 1:
    coin_toss = random.random()
    choice =(input("Enter your guess( Heads, Tails): "))
    if choice == "Heads" and coin_toss ==0.99:
        print("congratulations! you won!.")
    else:
        print("Sorry, you lost"+ ".")

elif input_method == 2:
    coin_toss=random.randint(0,1)
    choice =(input("Enter your guess( Heads, Tails): "))
    if choice == "Heads" and coin_toss == 1:
        print("congratulations! you won!.")
    else:
        print("Sorry, you lost"+ ".")   

else:
    print("Invalid choice. Please choose either 1 or 2.")

 