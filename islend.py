#area=input("chose an area:(cairo),(alexandria),(tanta) ")
#if area.lower()=="cairo" or area.lower()=="alexandria" or area.upper()=="TANTA":
#    print(f"you chose {area} and it is in the list ")
#else:
#    print(f"you chose {area} and it is not in the list ")


#age=int(input("enter your age: \n"))
#license=input("do you have Driver's license? (yes/no) \n")
#    print("you can drive")
#else:
#    print("you cannot drive")


#is_gordanian=input("Are you a gordanian? (yes/no) \n").lower()

#if is_gordanian=="yes":
#    print("good,that's first step.")
#   is_18=input("Are you above 18? type (yes/no) \n").lower()


#    if is_18=="yes":
#        print("you can hve an ID ")
#    else:
#        print("you cannot have an ID.")

#else:
#    print("sorry, an gordanian ID id give only to gordanians.")




print("""⋆༺𓆩☠︎︎𓆪༻⋆

""")
#show welcome message.

print("welcome to my islend")
#ask which door the user wants to open.

door = input("There are two doors in front of you.🚪 red door and 🚪 blue door.\n Which door do you want to open? (red/blue)").lower()

#red door true ,you found the room.

if door == "red":
    print("Great! now you entered the room.")


#ask which box the user wants to open
    box=input("you found threeboxes:white🎁,black🎁,green🎁\n which box do you want to open? ").lower()

#check which box the user opened and print the result.
#green box true, you found the treasure.

    if  box == "green":
        print("congratulations! you opened the green box and found a treasure💰")

#black box false, you found the spiders.

    elif box == "black":
        print("Oops!you openeed the box filled with spiders🕷️")
#white box false, you found the snakes.

    elif box == "white":
        print("Oops!you openeed the box filled with snakes🐍")
#else statement for invalid box choice.

    else:
        print("Invalid choice.")
#blue door false, you found the crocodiles.

elif door == "blue":
    print("Oops! you entered the room filled with crocodiles🐊")
#else statement for invalid door choice.

else:
    print("Invalid choice.")