board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    print("\n" + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + "\n" + 
        "---------" + "\n" + 
        str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + "\n" +
        "---------" "\n" +
        str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + "\n")

#win = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def x_win():
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        return True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        return True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        return True
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        return True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return True
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        return True
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        return True

def o_win():
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        return True
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        return True
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        return True
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        return True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return True
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        return True
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        return True

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

        
