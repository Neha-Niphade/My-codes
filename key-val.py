# Hash table using division method and chaining
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists for chaining

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists -> update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated: ({key}, {value}) at index {index}")
                return
        # Otherwise insert new pair
        self.table[index].append((key, value))
        print(f"Inserted: ({key}, {value}) at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                print(f"Found: key={key}, value={v} at index {index}")
                return v
        print("Key not found")
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                print(f"Deleted: key={key} from index {index}")
                return
        print("Key not found, cannot delete")

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

# Demonstration
ht = HashTable()

# Insert
ht.insert(10, "A")
ht.insert(20, "B")
ht.insert(25, "C")
ht.insert(35, "D")   # Collision with 25 (since 25 % 10 = 5, 35 % 10 = 5)

# Display table
ht.display()

# Search
ht.search(25)
ht.search(100)  # Not found

# Delete
ht.delete(25)
ht.display()
