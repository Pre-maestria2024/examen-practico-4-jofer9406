
def main():
    # Lee la primera línea con m y n
    m, n = map(int, input().split())
    # Lee la segunda línea con los m valores de H
    H = list(map(int, input().split()))
    # Lee la tercera línea con los m valores de D
    D = list(map(int, input().split()))
    
    # Suma total de dinero de todos los alimentos
    total_d = sum(D)
    
    # dp[j] = costo mínimo (en d_i) para llegar a salud j
    INF = 10**15
    dp = [INF]*(n+1)
    dp[0] = 0
    
    for i in range(m):
        hi, di = H[i], D[i]
        # Recorremos la salud en orden descendente
        for health in range(n, -1, -1):
            nuevo = min(n, health + hi)
            if dp[health] + di < dp[nuevo]:
                dp[nuevo] = dp[health] + di
    
    # Costo mínimo para alcanzar salud n
    min_cost = dp[n]
    # Máximo dinero que se puede obtener
    print(total_d - min_cost)


if __name__ == '__main__':
    main()

