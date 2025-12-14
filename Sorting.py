# ---------------------------
# Selection Sort
# ---------------------------
def selectionSort(arr, n):
    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        # swap
        arr[i], arr[mini] = arr[mini], arr[i]

    print("\nSalaries after Selection Sort:", arr)


# ---------------------------
# Bubble Sort
# ---------------------------
def bubbleSort(arr, n):
    for i in range(n-1):
        swapped=False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
        if(swapped==False):
            break

    print("\nSalaries after Bubble Sort:", arr)


# ---------------------------
# Main Program (Menu Driven)
# ---------------------------
arr = []
n = int(input("Enter total number of employees: "))

# Input salaries
arr = [0] * n
for i in range(n):
    arr[i] = float(input(f"Enter salary of employee {i+1}: "))

while True:
    print("\n------ MENU ------")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Display Top 5 Highest Salaries")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        selectionSort(arr, n)

    elif ch == 2:
        print()
        bubbleSort(arr, n)

    elif ch == 3:
        print("\nTop 5 Highest Salaries:")
        
        # IMPORTANT: array is already sorted by chosen algorithm
        top = 5
        if n < 5:
            top = n

        # print from end
        for i in range(n-1, n-top-1, -1):
            print(arr[i])

    elif ch == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
