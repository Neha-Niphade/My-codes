def avg_(members):
    if not members:
        print("No members")
        return
    avgg = my_sum(members) / my_len(members)
    print(avgg)


def my_sum(members):
    s = 0
    for k in members:       # k = key
        s = s + members[k]  # add value
    return s


def my_len(members):
    c = 0
    for _ in members:
        c = c + 1
    return c


def High_Low(books):
    if not books:
        print("No books added yet!")
        return

    most = None
    mostName = None
    least = None
    leastName = None

    for b in books:
        v = books[b]

        if most is None or v > most:
            most = v
            mostName = b

        if least is None or v < least:
            least = v
            leastName = b

    print("Most borrowed book:", mostName, "(", most, "times )")
    print("Least borrowed book:", leastName, "(", least, "times )")


def Zero_cnt(members):
    zero = 0
    for m in members:
        if members[m] == 0:
            zero = zero + 1
    print("#members with zero boc:", zero)


def Most_freq(books):
    if not books:
        print("No books")
        return

    # 1. find max value
    max_borrow = None
    for b in books:
        if max_borrow is None or books[b] > max_borrow:
            max_borrow = books[b]

    # 2. collect all books having that max value
    result = []
    for b in books:
        if books[b] == max_borrow:
            result = result + [b]      # no list comprehension

    print("Most frequently borrowed book(s):", result)


def Menu():
    books = {}
    members = {}

    while True:
        print("\n LIBRARY BORROW RECORD SYSTEM")
        print("1. Add Book Record")
        print("2. Add Member Record")
        print("3. avg_books by all memb")
        print("4. Highest n lowest Borrowing")
        print("5. Count members with 0 borrow cnt")
        print("6. Mode\n7. Exit")

        ch = int(input("Enter choice: "))

        if ch == 1:
            name = input("Enter book name:")
            books[name] = int(input("Enter times borrowed:"))

        elif ch == 2:
            name = input("Enter member name:")
            members[name] = int(input("Enter books borrowed:"))

        elif ch == 3:
            avg_(members)

        elif ch == 4:
            High_Low(books)

        elif ch == 5:
            Zero_cnt(members)

        elif ch == 6:
            Most_freq(books)

        elif ch == 7:
            break


Menu()
