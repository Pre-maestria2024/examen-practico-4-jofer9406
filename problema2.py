def main():
    import sys
    sys.setrecursionlimit(10**7)  # Para evitar problemas si el árbol es muy profundo.

    # Lee n y k
    n, k = map(int, input().split())

    # Construye la lista de adyacencias
    adjacency = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adjacency[u].append(v)
        adjacency[v].append(u)

    # Si n=0 o k=0, no hay grupos posibles
    if n == 0 or k == 0:
        print(0)
        return

    # Variable para contar el número de grupos
    ans = 0

    # DFS que retorna la “longitud de cadena” hacia arriba
    def dfs(u, parent):
        nonlocal ans
        max_chain_up = 0  # la mayor cadena que se puede seguir extendiendo hacia el padre
        for child in adjacency[u]:
            if child == parent:
                continue
            child_chain = dfs(child, u)
            # Si al sumar este nodo formamos una cadena de k, creamos un grupo
            if child_chain + 1 == k:
                ans += 1
            else:
                # De lo contrario, seguimos extendiendo la cadena
                max_chain_up = max(max_chain_up, child_chain + 1)
        return max_chain_up

    # Lanzamos DFS desde la raíz 0 (por defecto)
    dfs(0, -1)

    # Imprimimos cuántos grupos se lograron formar
    print(ans)

if __name__ == '__main__':
    main()
