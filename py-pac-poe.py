# Initialize Game State
board = [[[], [], [], ], [[], [], [],], [[], [], [],]]
players = ["X", "O"]
player = players[0]
winner = None

def show_board(board):
  print(f"""
  
      A   B   C
	
  1)  {str(board[0][0]).replace("'", "")} | {str(board[0][1]).replace("'", "")} | {str(board[0][2]).replace("'", "")} 
     -----------
  2)  {str(board[1][0]).replace("'", "")} | {str(board[1][1]).replace("'", "")} | {str(board[1][2]).replace("'", "")} 
     -----------
  3)  {str(board[2][0]).replace("'", "")} | {str(board[2][1]).replace("'", "")} | {str(board[2][2]).replace("'", "")} 


  """.replace("[]", " ").replace("[", "").replace("]", ""))

def convert_move(move):
  converted_move = move.replace("a", "0")
  converted_move = converted_move.replace("b", "1")
  return converted_move.replace("c", "2")

def check_valid_move(move):
  print("checkvalid called, move:", move)
  if len(move) == 2 and move.isnumeric() and not board[int(move[0]) - 1][int(move[1])]:
    return True

def claim_space(move, board, player):
  print("claimspace called")
  board[int(move[0]) - 1][int(move[1])] = player
  return board

def check_winner(board, player):
  # Check Horizontal Win
  for row in board:
    row_count = 0
    for cell in row:
      if cell == player:
        row_count += 1
        print("rowcount", row_count)
        if row_count == 3:
          return player

    # Check Vertical Win
    for num in range(0, 3):
      column_count = 0
      for row in board:
        if row[num] == player:
          column_count += 1
          print("colcount", column_count)
          if column_count == 3:
            return player

    # Check L-R Diagonal Win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
      return player
    # Check R-L Diagonal Win
    if board[0][0] == player and board [1][1] == player and board[2][2] == player:
      return player

    return None



while True:
  # Display the board:
  show_board(board)
  # Input Move:
  print(f"{player}'S TURN:")
  move = input("Please Input a Move: ")
  if move == "quit": break
  # Convert Move to Numerical Format:
  move = convert_move(move)
  # Check Move's Validity:
  if check_valid_move(move):
    # Change Board State:
    board = claim_space(move, board, player)
  else:
    print("\n" * 100)
    input("Invalid Move! <GO BACK TO MOVE INPUT & DON'T SWAP PLAYER>" )
  # Check for Winner:
  winner = check_winner(board, player)
  if winner:
    # Display win and init
    print("\n" * 100) 
    input(f"{player} wins!")
  else:
    # Change Player:
    player = players[players.index(player) - 1]
input("Goodbye!")

