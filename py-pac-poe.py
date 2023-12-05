# Initialize Game State
board = [[[], [], [], ], [[], [], [],], [[], [], [],]]
player = 1
winner = None


while True:
  # Display the board:
  # Input Move:
  # Convert Move:
  # Check Move's Validity:
  # Change Board State:
  # Check for Winner:
  # Change Player:
  return

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

  def convert_move(move):
    converted_move = move.replace("a", 0)
    converted_move = converted_move("b", 1)
    return converted_move.replace("c", 2)
