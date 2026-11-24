print("Welcome to place the rabbit")

field=[["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]
print(f"{field[0]} \n{field[1]} \n{field[2]}")

print("\nWhere should the rabbit ")

position=(input("please choose the rabbit go? 🐇  "))
row=int(position[0])
column=int(position[1])

field[row-1][column-1]="🐇"

print("\n Success....")

print(f"{field[0]} \n{field[1]} \n{field[2]}")



