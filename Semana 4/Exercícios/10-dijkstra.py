# leitura dos dados de entrada do EP
def minimo (Q, chave):
  min = -1 # inicializar min

  for i in range (len(Q)):
    if Q[i] == 1:
      if min == -1 or chave[i] < chave[min]:
         min = i

  return min #devolve indice de um vertice  

def extraiMinimo (Q, chave):
  min = minimo(Q, chave)
  Q[min] = 0
  return min   #devolve indice de um vertice

def vazio (Q):
  for i in range (len(Q)):
    if Q[i] == 1:
      return False
  return True

def relax(u,v,d,pi):
    weight = matrizAdj[u][v]
    if weight > 0:
      # Relax (u,v,w)
      if d[u] + weight < d[v]:
        d[v] = d[u] + weight
        pi[v] = u

n, m, s = (int(tmp) for tmp in input().split(" "))

# cria matriz de adjacencia com zeros
matrizAdj = [[0 for col in range(n)] for row in range(n)]

for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  # marca arco com o peso
  matrizAdj[i][j] = peso

# inicializacao
INF = 999999
NIL = -1
d = [0] * n
pi = [0] * n
for i in range (0, n):
  d[i] = INF
  pi[i] = NIL
d[s] = 0
Q = [1] * n    # todos na fila de prioridade

while not vazio(Q):
  u = extraiMinimo(Q, d)
  for v in range(n):
    relax(u,v,d,pi)

print(d)
print(pi)