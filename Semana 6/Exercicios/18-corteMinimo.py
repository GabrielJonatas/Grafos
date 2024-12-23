# Inserção no fim
def insere(Q, x):
    Q.append(x)

# Remove do início (assume fila não vazia)
def remove(Q):
    return Q.pop(0)

# Verifica se a fila está vazia
def vazio(Q):
    return len(Q) == 0

# Obtém as listas de adjacência (da matriz de adjacências)
def calculaListasAdjacencia(matrizAdj, n):
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            peso = matrizAdj[i][j]
            if peso > 0:
                adj[i].append([j, peso])
    return adj

# alterado para corte minimo
def bfs (matrizAdj, n, s):
  adj = calculaListasAdjacencia (matrizAdj, n)
  # inicializacao
  NIL = -1
  BRANCO = 1
  CINZA = 2
  PRETO = 3
  pi = [NIL] * n
  cor = [0] * n
  for v in range (0, n):
    cor[v] = BRANCO
  cor[s] = CINZA
  Q = []
  insere (Q, s)
  # marca vértices atingíveis a partir de s
  atingiveis = [0] * n
  # busca em largura
  while not vazio (Q):
    u = remove (Q)
    atingiveis[u] = 1
    for v, peso in adj[u]:
      if cor[v] == BRANCO:
        pi[v] = u
        cor[v] = CINZA
        insere (Q, v)
    cor[u] = PRETO
  return pi, atingiveis

# Caminho aumentante
def caminhoAumentante(matrizAdj, n, s, t):
    pi, _ = bfs(matrizAdj, n, s)
    
    NIL = -1
    INF = 999999
    capacidadeAumentante = INF
    j = t
    P = []

    if pi[t] == NIL:
        return [], 0
    
    while j != NIL:
        i = pi[j]
        if i == NIL:  
            break
        peso = matrizAdj[i][j]
        P.insert(0, [i, j, peso])
        capacidadeAumentante = min(capacidadeAumentante, peso)
        j = i

    if capacidadeAumentante == INF:
        capacidadeAumentante = 0
    return P, capacidadeAumentante

def aumentaFluxo (matrizAdj, fluxo, P, capacidadeAumentante):
  # calcula fluxo usando caminho aumentante
  for i, j, peso in P:
    if matrizAdj[i][j] > 0:
      fluxo[i][j] += capacidadeAumentante
    else:
      fluxo[i][j] -= capacidadeAumentante
  # calcula rede residual usando o fluxo atualizado
  matrizAdjResidual = [[0 for col in range(n)] for row in range(n)]
  for i in range (n):
    for j in range (n):
      matrizAdjResidual[i][j] = matrizAdj[i][j]
  for i in range (n):
    for j in range (n):
      if fluxo[i][j] > 0:
        matrizAdjResidual[j][i] = fluxo[i][j]
        matrizAdjResidual[i][j] = matrizAdj[i][j] - fluxo[i][j]
  return fluxo, matrizAdjResidual

# Entrada de dados
n, m, s, t = (int(tmp) for tmp in input().split(" "))

# Cria matriz de adjacência com zeros
matrizAdj = [[0 for col in range(n)] for row in range(n)]

# Leia `m` arestas
for _ in range(m):
    u, v, peso = (int(tmp) for tmp in input().split(" "))
    matrizAdj[u][v] = peso

import copy
matrizAdjResidual = copy.deepcopy(matrizAdj)

P, capacidadeAumentante = caminhoAumentante (matrizAdjResidual, n, s , t)

# inicialmente o fluxo eh zero
fluxo = [[0 for col in range(n)] for row in range(n)]

# enqto existe P, aumenta fluxo
while capacidadeAumentante > 0:
  fluxo, matrizAdjResidual = aumentaFluxo (matrizAdj, fluxo, P, capacidadeAumentante)
  P, capacidadeAumentante = caminhoAumentante (matrizAdjResidual, n, s, t)

print(fluxo)
print(matrizAdjResidual)

pi, atingiveis = bfs (matrizAdjResidual, n, s)

matrizCorte = [[0 for col in range(n)] for row in range(n)]

soma = 0
for i in range(n):
  for j in range(n):
    if matrizCorte[i][j] > 0 and atingiveis[i] and not atingiveis[j]:
      soma += matrizAdj[i][j]
print (soma)

for i in range(n):
  for j in range(n):
    if matrizAdj[i][j] > 0 and atingiveis[i] != atingiveis[j]:
      matrizCorte[i][j] = 1
print (matrizCorte)