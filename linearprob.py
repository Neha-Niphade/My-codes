class hash_table:
    def __init__(self,size=10):
        self.size=size
        self.table=[None]*size

    def hash_fun(self,key):
        index=key%self.size
        return index
    
    def insert(self,key):
        index=self.hash_fun(key)
        original=index 
        while(self.table[index] is not None and self.table[index] != -2):
            index=(index+1)%self.size
            if(original==index):
                break
        self.table[index]=key

    def display(self):
        print("hash table")
        for i in range (self.size):
            if(self.table[i]==None):
                print("empty")
            elif self.table[i] == -2:
                print(f"{i}: deleted")
            else:
                print(i,":",self.table[i])
    def Search(self,key):
        index = self.hash_fun(key)
        start = index

        while self.table[index] != None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}")
                return True
            index = (index + 1) % self.size
            if index == start:
                break
        print(f"Key {key} not found")
        return False
    def delete(self, key):
        index = self.hash_fun(key)
        start = index

        while self.table[index] != None:
            if self.table[index] == key: 
                self.table[index] = -2  
                print(f"Key {key} deleted from index {index}")
                return
            index = (index + 1) % self.size
            if index == start:
                break
        print(f"Key {key} not found to delete")
size=10        
ht=hash_table(size)
while True:
    print("operations:1.insert 2.display 3.delete 4.Search 5.Exit\n")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        key=int(input("Enter key:"))
        ht.insert(key)
    elif(ch==2):
        ht.display()
    elif(ch==3):
        key=int(input("Enter key to delete:"))
        ht.delete(key)
    elif(ch==4):
        key=int(input("Enter key to search"))
        ht.Search(key)
    elif(ch==5):
        print("Exiting")
        break
    else:
        print("Invalid choice")
