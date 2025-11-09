''' Implement a real-time event processing system using a Queue data structure. The system
 • Add an Event
 • Process the Next Event: The system should process and remove the event that has been in the queue the longest.
 • Display Pending Events: Show all the events currently waiting to be processed.
 • Cancel an Event: An event can be canceled if it has not been processed'''
Max=20
event_queue=[None]*Max
front=-1
rear=-1
def add_event():
    global event_queue,front,rear
    if rear==Max-1:
        print("Queue full")
        return
    event=input("enter name:")
    if(front==-1):
        front=0
    rear+=1
    event_queue[rear]=event
    print("Event added successfully")
def process_event():
    global event_queue,front,rear
    if(front==-1 or front>rear):
        print("No event to process")
        return
    value=event_queue[front]
    print("processing",value)
    front+=1
    if front > rear:
        front = rear = -1
def display_event():
    if rear==-1 or front>rear:
        print("No event to display")
        return
    i=front
    while(i<=rear):
        print(event_queue[i],end=" ")
        i+=1
    print()
def cancel_event():
    global front,rear,event_queue
    if (front==-1 or front>rear):
        print("No event in queue:")
        return
    event=input("Enter the name of the event to cancel:")
    i=front
    pos=-1
    while(i<=rear):
        if(event_queue[i]==event):
            pos=i
            break
        i+=1
    if pos==-1:
        print("Event not found")
        return
    while i<rear:
        event_queue[i]=event_queue[i+1]
        i+=1
    rear-=1
    if front>rear:
        front=-1
        rear=-1
    print(f"Event {event} cancelled")
        
def Menu():
    while True:
        print("1.Add 2.Process 3.Display 4.Cancel 5.Exit")
        ch=int(input("Enter ur choice:"))
        if ch==1:
            add_event()
        elif ch==2:
            process_event()
        elif ch==3:
            display_event()
        elif ch==4:
            cancel_event()
        elif ch==5:
            print("Exiting..")
            break
        else:
            print("Invalid input")
Menu()
