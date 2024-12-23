def matrizAdj(n,m):
    # cria matriz de adjacencia com zeros
    matrizAdj = [[0 for col in range(n)] for row in range(n)]
    for i in range (0, m):
        i, j = (int(tmp) for tmp in input().split(" "))
        # marca arco com 1
        matrizAdj[i][j] = 1
    return matrizAdj

def transposta(n,m):
    matrizAdjs = matrizAdj(n,m)
    # imprime listas de adjacencias
    for j in range (0, n):
        saida = "%d: " % j
        for i in range (0, n):
            if matrizAdjs[i][j] > 0:
                saida += "%d " % i
        print (saida)

n, m = (int(tmp) for tmp in input().split(" "))
transposta(n,m)