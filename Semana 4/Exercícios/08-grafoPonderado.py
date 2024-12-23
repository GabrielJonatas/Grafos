def grafoPonderado():
    n, m = (int(tmp) for tmp in input().split(" "))
    vetor = [[] for _ in range(n)]
    for i in range(m):
        v, u, w = (int(tmp) for tmp in input().split(" "))
        vetor[v].append([u,w])
    for k in range(n):
        texto = str(k) + ": "
        for n in range(len(vetor[k])):
            texto += str(vetor[k][n][0]) + "(" +  str(vetor[k][n][1]) + ") "
        print(texto)

grafoPonderado()