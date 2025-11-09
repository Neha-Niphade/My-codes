class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    return root


def search(root, key):
    if root is None or root.key == key:
        return root
    if key > root.key:
        return search(root.right, key)
    return search(root.left, key)


def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


def del_node(root, key):
    if root is None:
        print("Key not found.")
        return root

    if key < root.key:
        root.left = del_node(root.left, key)
    elif key > root.key:
        root.right = del_node(root.right, key)
    else:
        # KEY FOUND → print message
        print(f"Key {key} deleted successfully.")

        # Case 1: No left child
        if root.left is None:
            return root.right

        # Case 2: No right child
        elif root.right is None:
            return root.left

        # Case 3: Two children
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)

    return root


# -------- Menu Driven Program --------
if __name__ == "__main__":
    root = None

    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1. Insert a key")
        print("2. Display (Inorder Traversal)")
        print("3. Search a key")
        print("4. Delete a key")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            root = insert(root, key)
            print(f"Inserted {key} successfully.")

        elif choice == 2:
            print("Inorder traversal of BST:")
            inorder(root)
            print()

        elif choice == 3:
            key = int(input("Enter key to search: "))
            if search(root, key):
                print(f"Key {key} found in the tree.")
            else:
                print(f"Key {key} not found.")

        elif choice == 4:
            key = int(input("Enter key to delete: "))
            root = del_node(root, key)

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
