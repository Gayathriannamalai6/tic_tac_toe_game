def printing_board(position):
    print("-------------")
    print("| " + position[0] +" | " + position[1] +" | " + position[2] +" |")
    print("-------------")
    print("| " + position[3] +" | " + position[4] +" | " + position[5] +" |")
    print("-------------")
    print("| " + position[6] +" | " + position[7] +" | " + position[8] +" |")
    print("-------------")


def check_win(position,player):
    if ( position[0] ==player and position[1]==player and position[2]==player) or \
    ( position[3] ==player and position[4]==player and position[5]==player) or \
    ( position[0] ==player and position[3]==player and position[6]==player) or \
    ( position[1] ==player and position[4]==player and position[7]==player) or \
    ( position[2] ==player and position[5]==player and position[8]==player) or \
    ( position[0] ==player and position[4]==player and position[8]==player) or \
    ( position[2] ==player and position[4]==player and position[6]==player):
        return True
    else:
        False
        
def check_tie(position):
    if " " not in position:
        return True
    else:
        return False
    
def tic_tac_toe():
    position=[" "for _ in range(9)]
    player ="X"
    printing_board(position)

    while True:
        move = input("It's "+ player +"'s turn.please enter your choice of position(1-9): ")
        move = int(move)- 1


        if position[move] ==" ":
            position[move] = player
            printing_board(position)

            if check_win(position,player):
                print("Congrats!! Player" +player +" wins!")
                break
            elif check_tie(position):
                print("It's a tie!!")
                break
            else:
                player ="0" if player =="X" else "X"

        else:
            print("The position is already taken.Try any other position.")
tic_tac_toe()                   