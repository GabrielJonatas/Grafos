# Insercao no fim.
def insere (Q, x):
  Q.append (x)

# Remove do inicio.
# Assume fila nao vazia.
def remove (Q):
  return Q.pop (0)

# Devolve verdadeiro se fila vazia.
def vazio (Q):
  return len (Q) == 0

def criarAdj(n,m):
    adj = [[] for _ in range(n)]
    for k in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        adj[i].append(j)
    return adj

# algortimo bfs
def bfs(n,m,s, adj):
    # inicializacao
    d = [0] * n
    cor = [0] * n
    INF = 999999
    BRANCO = 1
    CINZA = 2
    PRETO = 3
    for v in range (n):
        d[v] = INF
        cor[v] = BRANCO
    d[s] = 0

    Q = [s]

    while not vazio (Q):
        u = remove (Q)
        for v in adj[u]:
            if cor[v] == BRANCO:
                d[v] = d[u] + 1
                cor[v] = CINZA
                insere (Q, v)
        cor[u] = PRETO

    return d

def matrizDeDistancias():
    n, m = (int(tmp) for tmp in input().split(" "))
    adj = criarAdj(n,m)
    for i in range(n):
        d = bfs(n,m,i,adj)
        texto = str(i) + ": "
        for j in range(n):
            texto += str(d[j]) + " "
        print(texto)

matrizDeDistancias()
