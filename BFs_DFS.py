# ---------- INPUT ----------
v = int(input("Enter number of vertices: "))

adjm = [[0]*v for _ in range(v)]        # adjacency matrix for DFS
adjl = [[-1]*v for _ in range(v)]       # adjacency list for BFS
degree = [0]*v                          # each node's neighbour count

# ---------- ADD EDGE ----------
def add_edge(u, w):
    adjm[u][w] = 1
    adjm[w][u] = 1

    adjl[u][degree[u]] = w
    degree[u] += 1

    adjl[w][degree[w]] = u
    degree[w] += 1


# ---------- DFS (Adjacency Matrix) ----------
def dfs(start):
    visited = [False]*v
    res = [0]*v
    c = 0

    stack = [0]*v
    top = -1

    # push start
    top += 1
    stack[top] = start

    while top >= 0:
        node = stack[top]
        top -= 1
        
        if not visited[node]:
            visited[node] = True
            res[c] = node
            c += 1

        # push neighbours in reverse order
        i = v - 1
        while i >= 0:
            if adjm[node][i] == 1 and not visited[i]:
                top += 1
                stack[top] = i
            i -= 1

    print("DFS:", end=" ")
    i = 0
    while i < c:
        print(chr(res[i] + 65), end=" ")
        i += 1
    print()


# ---------- BFS (Adjacency List) ----------
def bfs(start):
    visited = [False]*v
    res = [0]*v
    c = 0

    queue = [0]*v
    f = 0
    r = -1

    # enqueue start
    r += 1
    queue[r] = start
    visited[start] = True

    while f <= r:
        node = queue[f]
        f += 1

        res[c] = node
        c += 1

        i = 0
        while i < degree[node]:
            nei = adjl[node][i]
            if not visited[nei]:
                r += 1
                queue[r] = nei
                visited[nei] = True
            i += 1

    print("BFS:", end=" ")
    i = 0
    while i < c:
        print(chr(res[i] + 65), end=" ")
        i += 1
    print()


# ---------- MENU ----------
while True:
    print("\n1. Add Edge")
    print("2. DFS Traversal")
    print("3. BFS Traversal")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        u = int(input("Enter first vertex (0-based): "))
        w = int(input("Enter second vertex (0-based): "))
        add_edge(u, w)

    elif ch == 2:
        s = int(input("Enter start vertex: "))
        dfs(s)

    elif ch == 3:
        s = int(input("Enter start vertex: "))
        bfs(s)

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
