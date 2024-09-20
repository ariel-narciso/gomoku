from gomoku import Gomoku, PLAYER_ONE, PLAYER_TWO

CHAR_PLAYERS = [PLAYER_ONE, PLAYER_TWO]

class Connection:
  __whoPlays = 1
  __qtdClients = 0
  __clientWinner: (int | None) = None
  __game: Gomoku = None

  def __init__(self, game: Gomoku):
    self.__game = game

  def initConnection(self):
    self.__qtdClients += 1
    return (str(self.__game), self.__qtdClients)
  
  def myTime(self, client_id: int):
    grid = str(self.__game)
    if self.__clientWinner:
      return self.__clientWon(grid)
    return (
      grid,
      self.__qtdClients == 2 and
      self.__whoPlays == client_id
    )
  
  def __clientWon(self, grid: str):
    clientWinner = self.__clientWinner
    self.__qtdClients -= 1
    if self.__qtdClients == 0:
      self.__clientWinner = None
      self.__whoPlays = 1
      self.__game.resetGrid()
    return (grid, clientWinner)
  
  def myPlay(self, client_id: int, pos: tuple[int,int]):
    if self.__whoPlays != client_id or self.__clientWinner:
      return
    play = self.__game.makePlay(
      pos, CHAR_PLAYERS[self.__whoPlays - 1]
    )
    if play:
      if self.__game.verifyWinner():
        self.__clientWinner = self.__whoPlays
      self.__whoPlays = self.__whoPlays % 2 + 1
    return str(self.__game)
