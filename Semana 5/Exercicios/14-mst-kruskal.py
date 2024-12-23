def findSet (S, x):
  for i in range (len(S)):
    for j in S[i]:
      if j == x:
        return i

def makeSet (S, x):
  S.append([x])

def union (S, x, y):
  i = findSet (S, x)
  j = findSet (S, y)
  S[i] += S[j]
  S[j].clear()


n, m = (int(tmp) for tmp in input().split(" "))

# cria matriz de adjacencia com zeros
matrizAdj = [[0 for col in range(n)] for row in range(n)]

for i in range (0, m):
  i, j, peso = (int(tmp) for tmp in input().split(" "))
  # marca arco com o peso
  matrizAdj[i][j] = peso

arestas = []
for i in range (n):
  for j in range (n):
    if matrizAdj[i][j] > 0:
      peso = matrizAdj[i][j]
      arestas.append([i,j,peso])

# inicializacao
T = []   # arvore geradora inicialmente vazia
S = []
S = []
for i in range (0, n):
  makeSet (S, i)
# ordena arestas por peso crescente
import numpy as np
tmp = np.array(arestas)
ordenado = tmp[tmp[:, 2].argsort()]
for u,v,peso in ordenado:
  if findSet (S, u) != findSet (S, v):
    union (S, u, v)
    T.append ([u,v,peso])
print (T)

