def init():
  board = [
  [[], [], [],],
  [[], [], [],],
  [[], [], []]
  ]
  player = 1
  winner = None
  while True:
    gameloop()
  input("Goodbye!")

  def gameloop():
    #showboard
    
    move = lower(input("Please enter your next move: "))
    if move == "quit": break
    #checkvalid
    #claimspace
    #checkwin
    player *= 1
    #clear screen (or newline spam)




