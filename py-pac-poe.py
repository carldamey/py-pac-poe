player = None
board = None
winner = None
playing = None

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
  print()
  

def game_loop(player, board, winner):
  global playing
  print("gameloop called")
  show_board(board)
  
  move = input("Please enter your next move: ".lower())
  if move == "quit":
    playing = False
    return
  #checkvalid
  #claimspace
  #checkwin
  player *= -1
  #clear screen (or newline spam)

def show_board(board):
  print(f"""
      A   B   C
	
  1)  {board[0][0]} | {board[0][1]} | {board[0][2]} 
      -----------
  2)  {board[1][0]} | {board[1][1]} | {board[1][2]} 
      -----------
  3)  {board[2][0]} | {board[2][1]} | {board[2][2]} 


  """)

init()
print("init finished, playing is", playing)
while playing:
  game_loop(player, board, winner)
input("Goodbye!")
