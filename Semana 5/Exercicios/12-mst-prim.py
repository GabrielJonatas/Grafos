def vazio (Q):
  for i in range (len(Q)):
    if Q[i] == 1:
      return False
  return True

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


n, m, r = (int(tmp) for tmp in input().split(" "))

# cria matriz de adjacencia com zeros
matrizAdj = [[0 for col in range(n)] for row in range(n)]

for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  # marca arco com o peso
  matrizAdj[i][j] = peso

INF = 999999
NIL = -1
chave = [0] * n
pi = [0] * n
for i in range (0, n):
  chave[i] = INF
  pi[i] = NIL
chave[r] = 0
Q = [1] * n    # todos na fila de prioridade

while not vazio(Q):
  u = extraiMinimo(Q, chave)
  for v in range(n):
    weight = matrizAdj[u][v]
    if weight > 0:
      if(Q[v] == 1 and weight < chave[v]): 
        chave[v] = weight
        pi[v] = u

print(chave)
print(pi)