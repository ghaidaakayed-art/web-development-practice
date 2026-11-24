import random 
import string

#تجهيز القوائم
Prefixes=["Shadow", "Ghost", "Pro", "Ninja", "Wolf", "King", "Sniper"]
letter=list(string.ascii_letters)
number=list(string.digits)

#رسالة الترحيب

print("Welcome to the Username Generator! \n")


#السؤال عن طول الاسم

total_name=int(input("Enter the total number of characters in the username: "))

#السؤال عن عدد الارقام والاحرف

numbers=int(input("Enter the number of numbers in the username:"))
letters=int(input("Enter the number of letters in the username:"))

if letters + numbers != total_name:
    print("\nInvalid input. the sum of letters,numbers, and prefixes doesn't match the username ")

else:
    username=[]
    chosen_prefix = random.choice(Prefixes)

    for i in range(letters):
        username.append(random.choice(letter))

    for i in range(numbers):
        username.append(random.choice(number))


    random.shuffle(username)
    name=chosen_prefix + "".join(username)
    print(f"Generator username: {name}")
