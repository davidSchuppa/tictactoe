#num2 = [" "]*9
num = [[" "]*9,[" "]*9,[" "]*9,[" "]*9,[" "]*9,[" "]*9,[" "]*9,[" "]*9,[" "]*9]
player1 = input("PLAYER1: ")
player2 = input("PLAYER2: ")

def alak():
    print(
    """
      1   2   3   4   5   6   7   8   9
    1 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    2 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    3 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    4 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    5 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    6 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    7 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    8 {} | {} | {} | {} | {} | {} | {} | {} | {}
     -----------------------------------
    9 {} | {} | {} | {} | {} | {} | {} | {} | {}

    """.format(*num[0],*num[1],*num[2],*num[3],*num[4],*num[5],*num[6],*num[7],*num[8]))


def gamewon(stm1,val,stm2,val2):
    global num
    counter = 0
    j = 0
    l = 0
    k = 0
    while k < 9:
        if num[stm1 + j][stm2+l] == mark:
            counter = counter + 1
            if counter == 4:
                print(name.upper() +"! WINNER,WINNER,CHICKEN DINNER")
                raise NameError
        else:
            counter = 0
        j = j + val
        if stm1 + j < 0:
            raise IndexError
        l = l + val2
        if stm2 + l < 0:
            raise IndexError
        k = k + 1


alak()

while True:
    player_turn_counter = -1
    try:
        while True:
            if player_turn_counter == -1:
                mark ="x"
                name = player1
            else:
                mark ="0"
                name = player2

            inp = input(name+"\'s move: ")
            if inp == "q":
                raise NameError
                
            else:
                oszlop = int(inp[0]) - 1
                sor = int(inp[1]) - 1
                if num[oszlop][sor] == " ":
                    num[oszlop][sor] = mark
                    alak()
                    player_turn_counter *= -1

                    gamewon(0,1,sor,0)
                    gamewon(oszlop,0,0,1)
                    try:
                        gamewon(oszlop,1,sor,1)
                    except IndexError:
                        try:
                            gamewon(oszlop,-1,sor,-1)
                        except IndexError:
                            pass
                            
                    finally:
                        try:
                            gamewon(oszlop,1,sor,-1)
                        except IndexError:
                            try:
                                gamewon(oszlop,-1,sor,1)
                            except IndexError:
                                pass
                
    except NameError:
        break     
    except:
        continue