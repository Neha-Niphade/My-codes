class Library:
    def __init__(self):
        self.records=[]
    def input_records(self):
        n=int(input("Enter the total no. of library members:"))
        for i in range(n):
            count=int(input(f"Enter the no. of book borrowed by member {i+1}:"))
            self.records.append(count)
            print("records added successfully")
    
    def compute_avg(self):
        if not self.records:
            print("no data ava")
            return
        avg=sum(self.records)/len(self.records)
        print(avg)
    
    def highest_lowest(self):
        if not self.records:
            print("no data ava")
            return
        print(f"highest:{max(self.records)}")
        print(f"lowest:{min(self.records)}")
        
    def count_zero_borrowers(self):
        print(f"Members with 0 books: {self.records.count(0)}")
        
    def find_mode(self):
    freq = {}
    for count in self.records:
        freq[count] = freq.get(count, 0) + 1

    mode = max(freq, key=freq.get)
    print(f"Most frequent borrow count (Mode): {mode}")


        
def Main():
    lib=Library()
    while(True):
        print("\n---- Menu ----")
        print("1.Input  2.Avg  3.High/Low  4.Zero  5.Mode  6.Summary  7.Exit")
        ch=int(input("Enter ur choice:"))
        
        if(ch==1):
            lib.input_records()
        elif(ch==2):
            lib.compute_avg()
        else:
            print("invalid choice pls try again")
            
if __name__=="__main__":
    Main()
