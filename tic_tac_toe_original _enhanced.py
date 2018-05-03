board = list(range(1,10))

def draw_board():
    print(""" 
        {} | {} | {}   
        ---------  
        {} | {} | {}   
        ---------  
        {} | {} | {}""".format(*board))

def win():
    for i in range(0, len(board), 3):
        if len(set(board[i:i+3])) == 1:
            print("win")
    for i in range(0, 3):
        if len(set(board[i::3])) == 1:
            print("win")
    if len(set(board[0::4])) == 1:
        print("win")
    elif len(set(board[2:7:2])) == 1:
        print("win")



#X turn

def p1_turn():
    p1 = input("Player 1! Enter a number for the desired slot: ")
    p1 = int(p1)

    if p1 > 9 or p1 < 0:
        p1 = input("Enter a number between 1-9: ")
        p1 = int(p1)
        board[p1-1] = "X"
        draw_board()
    elif board[p1-1] == "O":
        p1 = input("Player 1! Enter another slot: ")
        p1 = int(p1)
        board[p1-1] = "X"
        draw_board()
    else:   
        board[p1-1] = "X"
        draw_board()

#O turn

def p2_turn():
    p2 = input("Player 2! Enter a number for the desired slot: ")
    p2 = int(p2)

    if p2 > 9 or p2 < 0:
        p2 = input("Enter a number between 1-9: ")
        p2 = int(p2)
        board[p2-1] = "O"
        draw_board()    
    elif board[p2-1] == "X":
        p2 = input("Player 2! Enter another slot: ")
        p2 = int(p2)
        board[p2-1] = "O"
        draw_board()
    else:
        board[p2-1] = "O"
        draw_board()

#check if board is full

def full_board():
    fullx = board.count("X")
    fullo = board.count("O")
    if fullx + fullo == 9:
        return True
    

draw_board()

#START GAME

while True:
    while True:
        try:
            p1_turn()
            break
        except:
            print("Error! Please enter a valid input!")
        

    x_win()
    if x_win() == True:
        print("Player 1 wins!")
        break
    
    full_board()
    if full_board() == True:
        print("The board is full!")
        break

    try:
        p2_turn()
    except:
        print("Error! Please enter a valid input!")
        p2_turn()
    
    o_win()
    if o_win() == True:
        print("Player 2 wins!")
        break

        
