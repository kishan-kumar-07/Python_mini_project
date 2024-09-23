# Hey, my name is Kishan Kuamr Ihave created a tic tac toe game as my python mini project.
# play and enjoy it.



instructions ="""
The GAME BOARD:-
 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 

HERE ARE THE INSTRUCTIONS YOU HAVE TO FOLLOW :-

1. Write your input(position number) to play your chance.
2. You have to fill all the spots to get the result.
3. First player will get the chance to enter first.

"""

board=[]
for i in range(9):
    board.append(" ")

def printboard():
    game_board = f"""
     {board[0]} | {board[1]} | {board[2]}
    ---|---|---
     {board[3]} | {board[4]} | {board[5]}
    ---|---|---
     {board[6]} | {board[7]} | {board[8]}
    
    """
    print(game_board)


index_list=[]
def take_input(player_name):
    while True:
        x=int(input(f"{player_name} :- "))
        x-=1
        if 0<= x <10:
            if x in index_list:
                print("THIS SPOT IS ALREADY BEING USED. ")
                continue
            index_list.append(x) 
            return x
        print("Enter the position number 1-9 :- ")

def result(p1,p2):
    if (board[0] == board[1] == board[2] == "X" or
        board[1] == board[4] == board[7] == "X" or
        board[0] == board[4] == board[8] == "X" or
        board[2] == board[5] == board[8] == "X" or
        board[3] == board[4] == board[5] == "X" or
        board[2] == board[4] == board[6] == "X" or
        board[6] == board[7] == board[8] == "X" or
        board[0] == board[3] == board[6] == "X"):
        print(f"CONGRATULATION {p1} !!!. \nYOU WON !.")
        quit("THANK YOU FOR PLAYING THIS GAME")
    elif (board[0] == board[1] == board[2] == "o" or
        board[1] == board[4] == board[7] == "o" or
        board[0] == board[4] == board[8] == "o" or
        board[2] == board[5] == board[8] == "o" or
        board[3] == board[4] == board[5] == "o" or
        board[2] == board[4] == board[6] == "o" or
        board[6] == board[7] == board[8] == "o" or
        board[0] == board[3] == board[6] == "o"):
        print(f"CONGRATULATION {p2} !!!. YOU WON !.")
        quit("THANK YOU FOR PLAYING THIS GAME")

    


def main():
    print("          ")
    print("-----------------------------------------------------")
    print("| * * *     WELCOME TO TIC-TAC-TOE GAME     * * * |")
    print("-----------------------------------------------------")
    print("          ")
    print("          ")
    p1 =input("Enter the FIRST PLAYER name :- \n")
    p2=input("Enter the SECOND PLAYER name :- \n") 
    print(f"\n THANK YOU FOR JOINING {p1} and {p2}")
    print("-----------------------------------------")
    print(f"       | *   {p1} VS {p2}   * |       ")
    print("-----------------------------------------")

    print(instructions)
    print(f"{p1}'s sign would be - X ")
    print(f"{p2}'s sign would be  - O ")
    input("\n PRESS ENTER TO START THE GAME  :")

    printboard()

    for i in range(9):
        if i % 2 == 0:
            index= take_input(p1)
            board[index]="X"
        else:
            index = take_input(p2)
            board[index]="O"
        
        printboard()
        result(p1,p2)
    
    print("IT'S A TIE!!!, PLAY AGAIN.")
    
main()
