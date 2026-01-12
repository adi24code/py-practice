box=[['1','2','3'],['4','5','6'],['7','8','9']]
def display_box(box):
    for i in range(3):
        for j in range(3):
            if j==1:
               print(f"| {box[i][j]} |",end=" ")
            elif j==2:
             print(f"{box[i][j]}")
            else:
             print(f" {box[i][j]}",end=" ")
        if i!=2:
           print("---+---+---")
        else:
           print()
def change_value(n,player):
   n=str(n)
   for i in range(3):
      for j in range(3):
         if box[i][j]==n:
            box[i][j]=player
   return display_box(box)
def check_win(player):
    wins = [
        # rows
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        # columns
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        # diagonals
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]
    for combo in wins:
        if all(box[i][j] == player for i,j in combo):
            return True
    return False

print('''
░▀█▀   ░█░   ░█▀▀        ░▀█▀   ░█▀█   ░█▀▀        ░▀█▀   ░█▀█   ░█▀▀▀
░░█    ░█░   ░█░░        ░░█    ░█▀█   ░█░░        ░░█    ░█░█   ░█▀▀░
░░▀    ░▀░   ░▀▀▀        ░░▀    ░▀░▀   ░▀▀▀        ░░▀    ░█▀█   ░▀▀▀░

''')

player1='X'
player2='O'
remaining=[1,2,3,4,5,6,7,8,9]
print('Welcome to Tic Tac Toe, Enter the number where you want to place your symbol')
display_box(box)
while True:
    while True:
        try:
            print(f'Remaining positions {remaining}')
            player1_input=int(input("your tern 'X':"))
            if player1_input in remaining:
                break
            print("Invalid move.")
        except ValueError:
            print("Enter a number.")

    change_value(player1_input, player1)
    remaining.remove(player1_input)

    if check_win(player1):
        print("Player X Won!")
        break
    if not remaining:
        print("Draw!")
        break

    while True:
        try:
            print(f'Remaining positions {remaining}')
            player2_input = int(input("Your turn 'O': "))
            if player2_input in remaining:
                break
            print("Invalid move.")
        except ValueError:
            print("Enter a number.")

    change_value(player2_input, player2)
    remaining.remove(player2_input)

    if check_win(player2):
        print("Player O Won!")
        break
