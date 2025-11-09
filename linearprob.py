SIZE = 10
table = [None] * SIZE      # None = empty, -2 = deleted


# ---------------- HASH FUNCTION ----------------
def hash_fun(key):
    return key % SIZE


# ---------------- INSERT ----------------
def insert(key):
    index = hash_fun(key)
    start = index

    while table[index] is not None and table[index] != -2:
        index = (index + 1) % SIZE
        if index == start:
            print("Hash table is full!")
            return

    table[index] = key
    print(f"Inserted {key} at index {index}")


# ---------------- SEARCH ----------------
def search(key):
    index = hash_fun(key)
    start = index

    while table[index] is not None:
        if table[index] == key:
            print(f"Key {key} found at index {index}")
            return True
        index = (index + 1) % SIZE
        if index == start:
            break

    print(f"Key {key} not found")
    return False


# ---------------- DELETE ----------------
def delete(key):
    index = hash_fun(key)
    start = index

    while table[index] is not None:
        if table[index] == key:
            table[index] = -2    # mark as deleted
            print(f"Key {key} deleted from index {index}")
            return
        index = (index + 1) % SIZE
        if index == start:
            break

    print(f"Key {key} not found to delete")


# ---------------- DISPLAY ----------------
def display():
    print("\nHash Table:")
    for i in range(SIZE):
        if table[i] is None:
            print(i, ": empty")
        elif table[i] == -2:
            print(i, ": deleted")
        else:
            print(i, ":", table[i])
    print()


# ---------------- MENU ----------------
while True:
    print("\n1.Insert  2.Display  3.Delete  4.Search  5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif choice == 2:
        display()

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)

    elif choice == 4:
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
