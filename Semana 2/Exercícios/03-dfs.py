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
    tempo[0] += 1
    d[v] = tempo[0]
    cor[v] = CINZA
    for u in adj[v]:
        if cor[u] == BRANCO:
            visitaDFS(adj, d, f, cor, u, tempo)
    tempo[0] += 1
    f[v] = tempo[0]
    cor[v] = PRETO

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
    for v in range (n):
        if cor[v] == BRANCO:
            visitaDFS(adj, d, f, cor, v, tempo)
    print(d)
    print(f)

n, m = (int(tmp) for tmp in input().split(" "))
dfs(n,m)

