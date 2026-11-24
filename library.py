#colors=[]
#colors.append(input("add the first color you like : "))

#input("Do you want to add more colors? (yes/no) ")
#if input() == "yes":
#    colors.append(input("add another color to the list :"))
#    print(f"the color you like are: {colors}")

#else:
#    print(f"the color you like are: {colors}")


library=[]
wishlist=[]
name_book=input("Enter the name of a book you own : ")
library.append(name_book)

name_book2=input("Enter the name of another book you own (or press 'enter' to skip): ")
library.append(name_book2)
print(f"Your library: {library}")


name_book3=input("Enter the name of a book you wish to have : ")
wishlist.append(name_book3)

book_name4=input("Enter the name of another book you wish to have (or press 'enter' to skip): ")
wishlist.append(book_name4)
print(f"Your wish list: {wishlist}")



acquired_book=input("Enter the name of a book from your wishlist that you've acquired (or press 'enter' to skip): ")
if acquired_book in wishlist:
    library.append(acquired_book)
    wishlist.remove(acquired_book)
    
    print(f"update_library: {library}")
    print(f"update_wishlist: {wishlist}")


    donared_book=input("Enter the name of a book from your library you wish to donate (or press 'enter' to skip): ")
    
    if donared_book in library:
        library.remove(donared_book)
        print(f"final library after donations: {library}")
    else:
        print(f"your library is {library}.")

else:
    donared_book=input("Enter the name of a book from your library you wish to donate (or press 'enter' to skip): ")
    
    if donared_book in library:
       library.remove(donared_book)
       print(f"final library after donations: {library}")
    else:
        print(f"your library is {library}.")


