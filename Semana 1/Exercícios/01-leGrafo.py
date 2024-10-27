def leGrafo():
    n, m = (int(tmp) for tmp in input().split(" "))
    vetor = [[] for _ in range(n)]
    for i in range(m):
        v, u = (int(tmp) for tmp in input().split(" "))
        vetor[v].append(u)
    for k in range(n):
        texto = str(k) + ": "
        for n in range(len(vetor[k])):
            texto += str(vetor[k][n]) + " "
        print(texto)

leGrafo()