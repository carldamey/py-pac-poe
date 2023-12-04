player = None
board = None
winner = None
playing = None

def init():
  global player, board, winner, playing
  print("init called")
  board = [
  [[], [], [],],
  [[], [], [],],
  [[], [], []]
  ]
  player = 1
  winner = None
  playing = True
  print()
  

def game_loop(player, board, winner):
  global playing
  print("gameloop called")
  show_board()
  
  move = input("Please enter your next move: ".lower())
  if move == "quit":
    playing = False
    return
  #checkvalid
  #claimspace
  #checkwin
  player *= -1
  #clear screen (or newline spam)

def show_board():
  print(board)

init()
print("init finished, playing is", playing)
while playing:
  game_loop(player, board, winner)
input("Goodbye!")
