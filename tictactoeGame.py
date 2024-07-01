class TicTacToe:
    def __init__(self) -> None:
        # the _ indicates a temporary or throwaway variable
        self.board=[" " for _ in range(9)]
        self.currentWinner=None

    def print_board(self):
       for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
           print('| ' + ' | '.join(row) + " |")

    @staticmethod
    def print_board_nums():
     number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
     for row in number_board:
        for cell in row:
           print(cell)

    def available_moves(self):
       moves=[]
       #enumerate in python creates a list of tuples with [index, value] 
       # for(i, spot) in enumerate(self.board):
       #    if spot == ' ' :
       #       moves.append(i)
       # return moves
       #alternative syntax wirh list comprehension
       return [i for i, spot in enumerate(self.board) if spot == '']
    
def play(game, x_player, o_playyer, print_game=True):
    if print_game:
        game.print_board_nums()
    letter="X"
    