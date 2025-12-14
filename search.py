def Linear_search(cust_Id,search_Id,n):
    for i in range(n):
        if(cust_Id[i]==search_Id):
            return True
    return False    
def Binary_search(cust_Id,search_Id,n):
    low=0
    high=n-1
    while(low<=high):
        mid=low+(high-low)//2
        if(cust_Id[mid]==search_Id):
           return True
        elif(cust_Id[mid]<search_Id):
            low=mid+1
        else:
            high=mid-1
    return False
        
        
cust_Id=[]
n=int(input("Enter no. of customers:"))
for i in range(n):
    id=int(input(f"Enter customer id{i+1}:"))
    cust_Id.append(id)
print(cust_Id)

ch=int(input("Enter which search method to be used:\n1.Linear search \n2.Binary search:\n"))
search_Id=int(input('enter the id to be searched:'))
if(ch==1):
    if Linear_search(cust_Id,search_Id,n):
        print(f"Id{search_Id} found using linear Search")
    else:
        print("Not found")
elif(ch==2):
    cust_Id.sort()
    if Binary_search(cust_Id,search_Id,n):
        print(f"Id value {search_Id} found using Binary Search")
    else:
         print("Not found")
else:
    print("Invalid input")
