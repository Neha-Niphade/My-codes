class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        newnode = Node(roll, name, marks)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newnode

    def display(self):
        if self.head is None:
            print("No records found.")
            return
        print("\nRoll\tName\tMarks")
        t = self.head
        while t is not None:
            print(f"{t.roll}\t{t.name}\t{t.marks}")
            t = t.next

    def search(self, roll):
        t = self.head
        while t is not None:
            if t.roll == roll:
                print(f"Found: Roll={t.roll}, Name={t.name}, Marks={t.marks}")
                return
            t = t.next
        print("Record not found.")

    def delete(self, roll):
        if self.head is None:
            print("Empty list.")
            return
        if self.head.roll == roll:
            self.head = self.head.next
            print("Record deleted.")
            return
        prev = None
        t = self.head
        while t is not None and t.roll != roll:
            prev = t
            t = t.next
        if t is None:
            print("Record not found.")
            return
        prev.next = t.next
        print("Record deleted.")

    def update(self, roll):
        t = self.head
        while t is not None:
            if t.roll == roll:
                t.name = input("Enter new name: ")
                t.marks = int(input("Enter new marks: "))
                print("Record updated.")
                return
            t = t.next
        print("Record not found.")

    def sort(self, key="roll", order="asc"):
        if self.head is None:
            print("No records to sort.")
            return
        changed = True
        while changed:
            changed = False
            t = self.head
            while t.next is not None:
                first = t.roll if key == "roll" else t.marks
                second = t.next.roll if key == "roll" else t.next.marks
                if (order == "asc" and first > second) or (order == "desc" and first < second):
                    # swap all data
                    t.roll, t.next.roll = t.next.roll, t.roll
                    t.name, t.next.name = t.next.name, t.name
                    t.marks, t.next.marks = t.next.marks, t.marks
                    changed = True
                t = t.next
        print(f"Records sorted by {key} in {order} order.")


# --- Menu Driven ---
s = StudentList()

while True:
    print("\n1.Add  2.Display  3.Search  4.Delete  5.Update  6.Sort  7.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        r = int(input("Roll: "))
        n = input("Name: ")
        m = int(input("Marks: "))
        s.add(r, n, m)

    elif ch == 2:
        s.display()

    elif ch == 3:
        r = int(input("Enter roll to search: "))
        s.search(r)

    elif ch == 4:
        r = int(input("Enter roll to delete: "))
        s.delete(r)

    elif ch == 5:
        r = int(input("Enter roll to update: "))
        s.update(r)

    elif ch == 6:
        k = input("Sort by (roll/marks): ")
        o = input("Order (asc/desc): ")
        s.sort(k, o)
        s.display()

    elif ch == 7:
        break

    else:
        print("Invalid choice.")
