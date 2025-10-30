from collections import deque

loc = ['A', 'B', 'C', 'D', 'E']
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['B', 'C']
}
adj_matrix = [
   [0,1,1,0,0],
   [1,0,0,1,1],
   [1,0,0,0,1],
   [0,1,0,0,0],
   [0,1,1,0,0]
]
def bfs():
    q = deque(['A'])
    v = []
    while q:
        n = q.popleft()
        if n not in v:
            v.append(n)
            q.extend(adj_list[n])
    print("BFS:", '->'.join(v))

def dfs():
    visited = [0]*len(loc)
    def visit(i):
        visited[i] = 1
        print(loc[i], end=' ')
        for j in range(len(adj_matrix)):
            if adj_matrix[i][j] == 1 and not visited[j]:
                visit(j)
    visit(0)  
    print()
while True:
    print("\n1. BFS")
    print("2. DFS")
    print("3. Exit")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        bfs()
    elif ch == 2:
        print("DFS:", end=' ')
        dfs()
    elif ch == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
