MAX = 50
queue_call = [None] * MAX
front = -1
rear = -1

def addCall(customerID, callTime):
    global front, rear

    if rear == MAX - 1:
        print("Queue FULL! Cannot add more calls.")
        return


    if front == -1:
        front = 0

    rear += 1
    queue_call[rear] = {"customerID": customerID, "callTime": callTime}

    print(f"Call added: CustomerID = {customerID}, CallTime = {callTime} mins")



def answerCall():
    global front, rear

    if front == -1 or front > rear:
        print("No calls to answer.")
        return

    call = queue_call[front]
    print(f"Answered call: CustomerID = {call['customerID']}, CallTime = {call['callTime']} mins")

    front += 1

    # Queue becomes empty
    if front > rear:
        front = rear = -1



def viewQueue():
    if front == -1 or front > rear:
        print("Queue is empty.")
        return

    print("\nPending Calls:")
    i = front
    while i <= rear:
        call = queue_call[i]
        print(f"{i - front + 1}. CustomerID = {call['customerID']}, CallTime = {call['callTime']} mins")
        i += 1
    print()



def isQueueEmpty():
    if front == -1 or front > rear:
        print("Yes, the queue is empty.")
    else:
        print("No, there are calls waiting in the queue.")



def Menu():
    while True:
        print("\n---- Menu ----")
        print("1. Add Call")
        print("2. Answer Call")
        print("3. View Queue")
        print("4. Is Queue Empty?")
        print("5. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            customerID = int(input("Enter Customer ID: "))
            callTime = int(input("Enter Call Time (minutes): "))
            addCall(customerID, callTime)

        elif ch == 2:
            answerCall()

        elif ch == 3:
            viewQueue()

        elif ch == 4:
            isQueueEmpty()

        elif ch == 5:
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")



if __name__ == "__main__":
    Menu()
