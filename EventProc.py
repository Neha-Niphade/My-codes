event_queue=[]
def Add_Event():
    event=input("Enter name of the event:")
    event_queue.append(event)
    print(f"event {event} added successfully")
def Process_Event():
    if not event_queue:
        print("no event to process")
    else:
        pe=event_queue.pop(0)
        print(f"processing event {pe}")
def Display():
    if not event_queue:
        print(" No pending events.")
    else:
        print("Pending events:")
        for i,item in enumerate(event_queue,start=1):
            print(f"{i}.{item}")
def Cancel_Event():
    if not event_queue:
        print("No event to cancel")
        return
    else:
        e=input("Enter the name of the event to cancel")
        if e in event_queue:
            event_queue.remove(e)
            print(f"event {e} cancelled succesfully")
        else:
            print(f"event cancellation us")
            
    

def Menu():
    while(True):
        print("---Menu---")
        print("1.Add event\n 2.Process Event\n3.Display Event\n4.Cancel Event\n5.Exit")
        ch=int(input("Enter your choice:"))
        if(ch==1):
            Add_Event()
        elif(ch==2):
            Process_Event()
        elif(ch==3):
            Display()
        elif(ch==4):
            Cancel_Event()
        elif(ch==5):
            print("Exiting")
            break
        else:
            print("enter valid choice")
if __name__=="__main__":
    Menu()
