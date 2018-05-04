board = list(range(1, 10))
turn_counter = 1


def draw_board():
    print(""" 
        {} | {} | {}   
        ---------  
        {} | {} | {}   
        ---------  
        {} | {} | {}
        """.format(*board))


def win():
    for i in range(0, len(board), 3):
        if len(set(board[i:i+3])) == 1:
            return True
    for i in range(0, 3):
        if len(set(board[i::3])) == 1:
            return True
    if len(set(board[0::4])) == 1:
        return True
    elif len(set(board[2:7:2])) == 1:
        return True


draw_board()

# START GAME
while turn_counter <= 9:
    if turn_counter % 2 == 0:
        mark = "O"
    else:
        mark = "X"

    try:
        player = int(input("Player " + mark + "! Enter a number for the desired slot: ")) - 1
        assert player >= 0

        if str(board[player]).isnumeric():
            board[player] = mark
            draw_board()
        else:
            raise ValueError

    except (IndexError, ValueError, AssertionError):
        print("Error! Please enter a valid input!")
        continue

    if win():
        print("Win!!!")
        break

    turn_counter += 1
