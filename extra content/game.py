from player import Player
from board import Board

class Game:

    def __init__(self):
        print("I wanna play a game...")
        name1 = str(input("Give me a name of p1 (this player is X): "))
        name2 = str(input("Give me a name of p2 (this player is O): "))
        p1 = Player(name1, "X")
        p2 = Player(name2, "O")

        print(p1)
        print(p2)

        board = Board(7, 6)
        board.print_board()

        won = False

        while not won:
            selection = input(f"Give a number for the column")
            if not selection.isnumeric():
                print("WRONG!!! Just give a number loser.Dont try to outsmart me dumbass")
                continue
            column = int(selection) -1
            if board.is_valid_column(column):
                print("Bro... for real?? you really dont know how to play connect 4 do you?")
                continue
            
        row = board.empty_row_for_column(0)
        board.add_token(row, 0, "X")
        board.print_board()

game = Game()
