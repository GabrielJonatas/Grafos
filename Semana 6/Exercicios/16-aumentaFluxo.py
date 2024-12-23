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

# Algoritmo BFS com predecessores
def bfs(n, s, matrizAdj):
    adj = calculaListasAdjacencia(matrizAdj, n)
    d = [0] * n
    cor = [0] * n
    pi = [-1] * n  # Predecessores
    INF = 999999
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    for v in range(n):
        d[v] = INF
        cor[v] = BRANCO
    d[s] = 0
    Q = [s]

    while not vazio(Q):
        u = remove(Q)
        for v, peso in adj[u]:
            if cor[v] == BRANCO:
                d[v] = d[u] + 1
                pi[v] = u  # Registra o predecessor
                cor[v] = CINZA
                insere(Q, v)
        cor[u] = PRETO

    return pi  # Retorna os predecessores

# Caminho aumentante
def caminhoAumentante(matrizAdj, n, s, t):
    pi = bfs(n, s, matrizAdj)
    NIL = -1
    INF = 999999
    capacidadeAumentante = INF
    j = t
    P = []

    while j != NIL and pi[j] != NIL:
        i = pi[j]
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

P, capacidadeAumentante_ = caminhoAumentante(matrizAdj, n, s, t)

fluxo = [[0 for col in range(n)] for row in range(n)]
fluxo, matrizAdjResidual = aumentaFluxo(matrizAdj, fluxo, P, capacidadeAumentante_)

print (P)
print (capacidadeAumentante_)
print (fluxo)
print (matrizAdjResidual)