PLAYER_ONE = 'X'
PLAYER_TWO = 'O'
INITIAL_CHAR = '*'

class Gomoku:
  __grid: list[list[str]]
  __mapSize: int
  __sequenceSize: int
  
  def __init__(self, mapSize: int, sequenceSize: int):
    self.__mapSize = mapSize
    self.__sequenceSize = sequenceSize
    self.resetGrid()
  
  def resetGrid(self):
    self.__grid = []
    for i in range(self.__mapSize):
      self.__grid.append(list(INITIAL_CHAR * self.__mapSize))
  
  def verifyWinner(self):
    for i in range(self.__mapSize - self.__sequenceSize + 1):
      for j in range(self.__mapSize - self.__sequenceSize + 1):
        res = self.__verifyWinnerSubMap(i, j)
        if res:
          return res
  
  def makePlay(self, pos: tuple[int,int], player: str):
    i, j = pos
    if (
      i < 0 or i >= self.__mapSize or
      j < 0 or j >= self.__mapSize or
      self.__grid[i][j] != INITIAL_CHAR
    ):
      return False
    self.__grid[i][j] = player
    return True

  def __verifyWinnerSubMap(self, i: int, j: int) -> str | None:
    # ------------- verify row --------------
    for x in range(i, i + self.__sequenceSize):
      row = self.__grid[x]
      res = self.__verifyWinnerSequence(row[j:j+self.__sequenceSize])
      if res:
        return res
    # ----------------------------------------
    # ------------ verify colunm ------------
    for y in range(j, j + self.__sequenceSize):
      column = ''
      for x in range(i, i + self.__sequenceSize):
        column += self.__grid[x][y]
      res = self.__verifyWinnerSequence(column)
      if res:
        return res
      
    # -----------------------------------------
    # ----------- verify diagonal -------------
    diagonal = ''
    for count in range(self.__sequenceSize):
      diagonal += self.__grid[i + count][j + count]
    res = self.__verifyWinnerSequence(diagonal)
    if res:
      return res
    diagonal = ''
    y = j + self.__sequenceSize - 1
    for x in range(i, i + self.__sequenceSize):
      diagonal += self.__grid[x][y]
      y -= 1
    res = self.__verifyWinnerSequence(diagonal)
    if res:
      return res
    # -----------------------------------------

  def __verifyWinnerSequence(self, sequence: list[str]):
    if "".join(sequence) == PLAYER_ONE * self.__sequenceSize:
      return PLAYER_ONE
    if "".join(sequence) == PLAYER_TWO * self.__sequenceSize:
      return PLAYER_TWO
    
  def __str__(self) -> str:
    res = '{:>2}'.format('')
    for col in range(self.__mapSize):
      res += '{:>4}'.format(col + 1)
    res += '\n'
    for rowIndex in range(self.__mapSize):
      res += '{:>2}'.format(rowIndex + 1)
      for char in self.__grid[rowIndex]:
        res += '{:>4}'.format(char)
      res += '\n'
    return res
