import numpy as np

# Implementacao ingenua: lista ou array
# Q[0..n-1]: 0 nao esta na fila, 1 esta na fila
def vazio (Q):
  for i in range (len(Q)):
    if Q[i] == 1:
      return False
  return True

def insere (Q, i):
  Q[i] = 1

# Assume Q != vazio
def minimo (Q, chave):
  min = -1 # inicializar min

  for i in range (len(Q)):
    if Q[i] == 1:
      if min == -1 or chave[i] < chave[min]:
         min = i

  return min #devolve indice de um vertice  

# Assume Q != vazio
def extraiMinimo (Q, chave):
  min = minimo(Q, chave)
  Q[min] = 0
  return min   #devolve indice de um vertice

# Devolve 1 se v estiver na fila Q, 0 caso contrario.
def busca (Q, v):
  return Q[v]

n, k = (int(tmp) for tmp in input().split(" "))
tmp2 = list (int(tmp) for tmp in input().split(" "))
chave = np.array(tmp2)
q = [0] * n

for i in range(k):
    op = input ()
    if (len(op) > 1):
        op, j = op.split(" ")
    j = int (j)
    match op:
        case 'I':
            insere (q,j)
            print(q)
        case 'M':
            print(minimo (q, chave), chave [minimo (q, chave)], q)
        case 'E':
            chaveMinima = chave[minimo (q, chave)]
            print(extraiMinimo (q,chave), chaveMinima, q)
        case 'B':
            print(busca (q,j), q)
        case 'V':
            print (vazio(q), q)
