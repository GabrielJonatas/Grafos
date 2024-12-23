BRANCO = 1
CINZA = 2
PRETO = 3

def criaAdj(n,m):
    adj = [[] for _ in range(n)]
    for k in range(m):
        i, j = (int(tmp) for tmp in input().split(" "))
        adj[i].append(j)
    return adj

def visitaDFS(adj, d, f, cor, v, tempo):
    # descoberta
    saidaTexto = "(%d " % v
    tempo[0] += 1
    d[v] = tempo[0]
    cor[v] = CINZA
    for u in adj[v]:
        if cor[u] == BRANCO:
            saidaTexto += visitaDFS(adj, d, f, cor, u, tempo)
    # finaliza
    saidaTexto += "%d) " % v
    tempo[0] += 1
    f[v] = tempo[0]
    cor[v] = PRETO
    return saidaTexto

# algortimo dfs
def dfs(n,m):
    adj = criaAdj(n,m)
    # inicializacao
    d = [0] * n
    f = [0] * n
    cor = [0] * n
    for v in range (n):
        cor[v] = BRANCO
    tempo = [0]
    saidaTexto = ""
    for v in range (n):
        if cor[v] == BRANCO:
            saidaTexto += visitaDFS(adj, d, f, cor, v, tempo)
    print(saidaTexto)

n, m = (int(tmp) for tmp in input().split(" "))
dfs(n,m)

