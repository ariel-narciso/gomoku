import xmlrpc.client as client

server = client.ServerProxy('http://localhost:8000')

id: int
grid: list[list[str]]

grid, id = server.initConnection()
winner: (int | None) = None

if id == 1:
  print('Aguarde a conexão do outro jogador ...\n')
else:
  print('Aguarde a jogada do outro jogador ...\n')

while not winner:
  grid, myTime = server.myTime(id)
  if type(myTime) == int:
    winner = myTime
  elif myTime:
    print(grid)
    a, b = map(int, input("Faça sua jogada: ").split())
    grid = server.myPlay(id, (a - 1, b - 1))
    print('\n{}'.format(grid))
    print('Aguarde a jogada do outro jogador ...\n')

print('{}\nVencedor: Cliente {}'.format(grid, winner))
