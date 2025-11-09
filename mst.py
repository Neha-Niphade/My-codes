# Function to find minimum key value vertex not yet included in MST
def min_key(key, mst_set, n):
    min_val = 99999
    min_index = -1
    for v in range(n):
        if mst_set[v] == 0 and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

# Function to print the MST result
def print_mst(parent, graph, n):
    print("\nMinimum Spanning Tree (Pizza Delivery Path):")
    total_time = 0
    for i in range(1, n):
        print("From Location", parent[i], "to", i, "=> Time:", graph[i][parent[i]])
        total_time += graph[i][parent[i]]
    print("Total Minimum Delivery Time:", total_time)

# Function implementing Prim's algorithm
def prims_algorithm(graph, n):
    key = [9999] * n
    parent = [0] * n
    mst_set = [0] * n

    key[0] = 0      # Start from first location
    parent[0] = -1  # First node is root of MST

    for _ in range(n - 1):
        u = min_key(key, mst_set, n)
        mst_set[u] = 1

        for v in range(n):#scan graph
            if graph[u][v] != 0 and mst_set[v] == 0 and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    print_mst(parent, graph, n)

def main():
    graph = []
    n = 0

    while True:
        print("\n--- Pizza Delivery System (Using Prim's Algorithm) ---")
        print("1. Enter Locations and Time Matrix")
        print("2. Find Minimum Delivery Time Path")
        print("3. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            n = int(input("Enter number of locations: "))
            graph = []
            print("Enter time matrix (0 if no direct path):")
            for i in range(n):
                row = []
                for j in range(n):
                    val = int(input(f"Time from {i} to {j}: "))
                    row += [val]
                graph += [row]
            print("Time Matrix Recorded Successfully!")

        elif ch == 2:
            if n == 0:
                print("Please enter locations and time matrix first!")
            else:
                prims_algorithm(graph, n)

        elif ch == 3:
            print("Exiting... ")
            break

        else:
            print("Invalid choice! Please try again.")
main()
