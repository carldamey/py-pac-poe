player = None
board = None
winner = None
playing = None
move = None

def init():
  global player, board, winner, playing
  print("init called")
  board = [
  [[1], [2], [3],],
  [[4], [5], [6],],
  [[7], [8], [9]]
  ]
  player = 1
  winner = None
  playing = True
  move = ""
  print()
  

def game_loop(player, board, winner):
  global playing
  print("gameloop called")
  show_board(board)
  move = input("Please enter your next move: ".lower())
  if move == "quit":
    playing = False
    return
  convert_move()
  if not check_valid_move(board, move):
    print("Invalid move!, (find a way to go back to top of gameloop)")
  #claimspace
  #checkwin
  player *= -1
  #clear screen (or newline spam)

def show_board(board):
  print(f"""
      {player}'S TURN

      A   B   C
	
  1)  {board[0][0]} | {board[0][1]} | {board[0][2]} 
      -----------
  2)  {board[1][0]} | {board[1][1]} | {board[1][2]} 
      -----------
  3)  {board[2][0]} | {board[2][1]} | {board[2][2]} 

  """)


def convert_move():
  global move
  move = move.replace("a", "0")
  move = move.replace("b", "1")
  move = move.replace("c", "2")


def check_valid_move(board, move):
  if len(move) != 2 or not move.isalnum() or board[move[0][move[1]]]: return False
  else: return True

init()
print("init finished, playing is", playing)
while playing:
  game_loop(player, board, winner)
input("Goodbye!")
