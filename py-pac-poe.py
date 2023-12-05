# Initialize Game State
board = [[[], [], [], ], [[], [], [],], [[], [], [],]]
players = ["X", "O"]
player = players[0]
winner = None

def show_board(board):
  print("""



  """)

def convert_move(move):
  converted_move = move.replace("a", "0")
  converted_move = converted_move.replace("b", "1")
  return converted_move.replace("c", "2")

def check_valid_move(move):
  return

def claim_space(move, board, player):
  return

def check_winner(board, player):
  return


while True:
  # Display the board:
  show_board(board)
  # Input Move:
  print("player:", player)
  move = input("Please Input a Move: ")
  # Convert Move:
  move = convert_move(move)
  # Check Move's Validity:
  if check_valid_move(move):
    # Change Board State:
    claim_space(move, board, player)
  # Check for Winner:
  if check_winner(board, player):
    # Display win and init
    print(f"Player {player} wins")
  # Change Player:
  else:
    player = players[players.index(player) - 1]
input("Goodbye!")

"""
print board
input move.lower()
convert a b c in input to 0 1 and 2
if move is 2 characters, numeric, and not taken, 
  then board[move[0][move[1]]] = player
if check_win_conditions(board)
  input(player <> wins!)
  init and restart
else player *= 1
"""


