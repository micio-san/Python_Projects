from tictactoePlayer import RandomPcPlayer, HumanPlayer

class TicTacToe:
    def __init__(self) -> None:
        # the _ indicates a temporary or throwaway variable
        self.board=[" " for _ in range(9)] #=>[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.current_winner=None

    def print_board(self):
       for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
           print('| ' + ' | '.join(row) + " |")
    #
    @staticmethod
    def print_board_nums():
     number_board=[[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
     for row in number_board:
        celle = ""
        for cell in row:
           celle = celle + '| ' + cell + ' |'
        print(celle)

    def available_moves(self):
       moves=[]
       #enumerate in python creates a list of tuples with [index, value] 
       # for(i, spot) in enumerate(self.board):
       #    if spot == ' ' :
       #       moves.append(i)
       # return moves
       #alternative syntax with list comprehension
       return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
       return ' ' in self.board
    
    def num_empy_squares(self):
        return self.board.count()

    def winner(self, square, letter):
        #// floor division divides and round down 8:3=2,66666666666666 => 2
        row_index = square // 3
        #return range
        row= self.board[row_index*3: (row_index + 1)*3] 
        #check rows
        if all([spot == letter for spot in row]):
           return True
        col_ind= square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
           return True
         #0,2,4,6,8
        if square % 2 ==0:
           diagonal1 = [self.board[i] for i in [0,4,8]]
           if all([spot == letter for spot in diagonal1]) :
              return True
           diagonal2 = [self.board[i] for i in [2,4,6]]         
           if all([spot == letter for spot in diagonal2]): 
              return True
        return False   
    
    def make_move(self, square, letter):
       if self.board[square] == ' ':
          self.board[square]=letter
          if self.winner(square, letter):
             self.current_winner = letter 
          return True
       else:
          return False
    

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter="X"

    while game.empty_squares():
        if letter == "X":
            square= x_player.get_move(game)
        else:
            square= o_player.get_move(game)

        if game.make_move(square,letter):
           if print_game:
              print(letter + ' makes a move on square ' + str(square))
              game.print_board()
              if game.current_winner:
                 print(letter + ' has won')
                 return letter
              letter = "O" if letter == "X" else "X"
    if print_game:
        print('It\'s a tie!')    

# type of __name__ = __main__, it's the default name of 
# the file that runs and it's not imported, python first reads the files that are imported 
# completely.
if __name__ == '__main__':
   x_player = HumanPlayer("X")
   o_player = RandomPcPlayer("O")
   t=TicTacToe()
   play(t, x_player, o_player, True)

