# ---------------- CALL CENTER QUEUE SIMULATION ----------------

MAX = 50  # Maximum queue size
call_queue = [None] * MAX  # Array to store calls
front = -1
rear = -1


def addCall(customerID, callTime):
    global front, rear
    if rear == MAX - 1:
        print("Queue FULL! Cannot add more calls.")
        return

    if front == -1:  # First call
        front = 0

    rear += 1
    call_queue[rear] = [customerID, callTime]
    print(f"Call added: CustomerID={customerID}, CallTime={callTime} minutes.")


def answerCall():
    global front, rear
    if front == -1 or front > rear:
        print("No calls to answer.")
        return

    print(f"Answering Call: CustomerID={call_queue[front][0]}, CallTime={call_queue[front][1]} minutes.")
    front += 1

    # Reset queue if empty
    if front > rear:
        front = -1
        rear = -1


def viewQueue():
    if front == -1 or front > rear:
        print("No pending calls.")
        return

    print("Pending Calls in Queue:")
    i = front
    while i <= rear:
        print(f"CustomerID={call_queue[i][0]}, CallTime={call_queue[i][1]} minutes")
        i += 1


def isQueueEmpty():
    return front == -1 or front > rear


while True:
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cid = input("Enter Customer ID: ")
        time = int(input("Enter Call Time (minutes): "))
        addCall(cid, time)
    elif choice == 2:
        answerCall()
    elif choice == 3:
        viewQueue()
    elif choice == 4:
        if isQueueEmpty():
            print("Queue is EMPTY.")
        else:
            print("Queue is NOT EMPTY.")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
