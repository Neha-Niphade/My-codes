queue_call=[]
def addCall(customerId,callTime):
    call={"customerId":customerId,"callTime":callTime}
    queue_call.append(call)
    print(f"call added successfully for ID:{customerId} with call time {callTime}")
    
def answerCall():
    if not queue_call:
        print("No calls remaining to ans")
        return
    call=queue_call.pop(0)
    print(f"Answered call having custId:{call['customerId']} and callTiming:{call['callTime']}mins")

def viewQueue():
    if not queue_call:
        print("Yes,Queue is empty.\n")
        return
    for i,call in enumerate(queue_call,start=1):
        print(f"{i}.CustomerId:{call['customerId'] } having CallTime:{call['callTime']} mins")
def isQueueEmpty():
    if not queue_call:
        print("Queue is empty")
    else:
        print("No,there are calls in the Queue")

def Menu():
    while True:
        print("----Menu----")
        print("1.Add\n2.Ans Call\n3.view\n4.isqueueEmpty\n5.exit")
        ch=int(input("Enter choice:"))
        if(ch==1):
            customerId = int(input("Enter customer ID: "))
            callTime = int(input("Enter call time in minutes: "))
            addCall(customerId,callTime)
        elif(ch==2):
            answerCall()
        elif(ch==3):
            viewQueue()
        elif(ch==4):
            isQueueEmpty()
        else:
            print("Exiting..")
            break
if __name__=="__main__":
    Menu()
