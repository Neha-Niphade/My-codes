# Global variables
records = []
n = 0

def input_records():
    global records, n
    n = int(input("Enter total members: "))
    records = [0] * n      # fixed size list
    
    for i in range(n):
        x = int(input(f"Books borrowed by member {i+1}: "))
        records[i] = x
    
    print("Records added.")


def compute_avg():
    if n == 0:
        print("No data")
        return

    total = 0
    for i in range(n):
        total += records[i]

    avg = total / n
    print("Average =", avg)


def highest_lowest():
    if n == 0:
        print("No data")
        return

    highest = records[0]
    lowest = records[0]

    for i in range(n):
        if records[i] > highest:
            highest = records[i]
        if records[i] < lowest:
            lowest = records[i]

    print("Highest =", highest)
    print("Lowest =", lowest)


def zero_borrowers():
    count0 = 0
    for i in range(n):
        if records[i] == 0:
            count0 += 1
    print("Members with 0 borrowings =", count0)


def find_mode():
    if n == 0:
        print("No data")
        return

    freq = {}

    # build frequency table
    for i in range(n):
        val = records[i]
        if val not in freq:
            freq[val] = 1
        else:
            freq[val] += 1

    # find mode manually
    mode = None
    maxf = 0
    for key in freq:
        if freq[key] > maxf:
            maxf = freq[key]
            mode = key

    print("Mode =", mode)


def main():
    while True:
        print("\n1.Input  2.Avg  3.High/Low  4.Zero  5.Mode  6.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            input_records()
        elif ch == 2:
            compute_avg()
        elif ch == 3:
            highest_lowest()
        elif ch == 4:
            zero_borrowers()
        elif ch == 5:
            find_mode()
        elif ch == 6:
            break
        else:
            print("Invalid choice")

main()
