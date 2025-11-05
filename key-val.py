class Node:
     def __init__(self,key,value):
         self.key=key
         self.value=value
         self.next=None
SIZE=10
table=[None]*SIZE
def hash_func(key):
    return key%SIZE
def insert(key,value):
    i=hash_func(key)
    n=Node(key,value)
    if not table[i]:
        table[i]=n
    else:
        t=table[i]
        while(t.next):
            t=t.next
        t.next=n
    print("Inserted!")
def search(key):
    i=hash_func(key)
    t=table[i]
    while(t):
        if(t.key==key):
            print("Found, value:",t.value)
            return
        t=t.next
    print("not found")
def delete(key):
    i=hash_func(key)
    t,p=table[i],None
    while t:
        if(t.key==key):
            if not p:
                table[i]=t.next
            else:
                p.next=t.next
                
            print("Deleted!")
            return
        p,t=t,t.next
    print("Not found!")
def display():
    for i in range(SIZE):
        t=table[i]
        print(f"At index{i}: ",end=" ")
        while t:
            print(f"{t.key},{t.value}",end=" ")
            t=t.next
        print()
def Menu():
    while True:
        print("1.Insert\n2.Search\n3.Delete\n4.Display\n5.Exit")
        ch=int(input("Enter your choice:"))
        if(ch==1):
            key=int(input("Enter the key:"))
            value=input("Enter the value to insert:")
            insert(key,value)
        elif(ch==2):
            k=int(input("Enter the key:"))
            search(k)
        elif(ch==3):
            k=int(input("Enter the key:"))
            delete(k)
        elif(ch==4):
            display()
        elif(ch==5):
            print("Exiting")
            break
        else:
            print("Invalid choice!")
Menu()
        
    
    
        
        
