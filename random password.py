#import string
#sentence=input("\nPlease enter a sentence: ")
#new_sentence=""
#for i in sentence:
#    if i not in string.punctuation:
#        new_sentence+=i
#print("\n\n***here is the same sentence without punctuation***\n\n",new_sentence)


import random 
import string

letter=list(string.ascii_letters)
number=list(string.digits)
sambol=list(string.punctuation)

print("Welcome to the password Generator! \n")
total=int(input("Enter the total number of characters in the password: "))

letters=int(input("ENter the number of letters in the password: "))
numbers=int(input("ENter the numbers of numbers in the password: "))
sambols=int(input("ENter the number of sambols in the password: "))

if letters + numbers + sambols != total:
    print("\nInvalid input. the sum of letters,numbers, and symbole doesn't match the password ")

else:
    password_list=[]
    for i in range(letters):
        password_list.append(random.choice(letter))

    for i in range(numbers):
        password_list.append(random.choice(number))

    for i in range(sambols):
        password_list.append(random.choice(sambol))

random.shuffle(password_list)
password="".join(password_list)
print(f"Generator password: {password}")


