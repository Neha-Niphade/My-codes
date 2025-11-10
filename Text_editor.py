# -------------------------------------------
# STACK IMPLEMENTATION (NO INBUILT FUNCTIONS)
# -------------------------------------------

undo_stack = ["" for _ in range(100)]
redo_stack = ["" for _ in range(100)]

undo_top = -1
redo_top = -1

document = ""


# ------------------ PUSH -------------------
def push(stack, top, value):
    top = top + 1
    stack[top] = value
    return top


# ------------------ POP --------------------
def pop(stack, top):
    value = stack[top]
    top = top - 1
    return value, top


# ------------------ MAKE CHANGE ------------
def make_change():
    global document, undo_top, redo_top

    # Push current doc state to undo stack
    undo_top = push(undo_stack, undo_top, document)

    # clear redo stack manually
    redo_top = -1

    change = input("Enter text to add: ")

    # apply change
    document = document + change  
    print("Change applied.")


# ------------------ UNDO --------------------
def undo():
    global document, undo_top, redo_top

    if undo_top == -1:
        print("Nothing to undo!")
        return

    # Push current state onto redo stack
    redo_top = push(redo_stack, redo_top, document)

    # Pop previous state from undo stack
    document, undo_top = pop(undo_stack, undo_top)
    print("Undo performed.")


# ------------------ REDO --------------------
def redo():
    global document, undo_top, redo_top

    if redo_top == -1:
        print("Nothing to redo!")
        return

    # Push current state to undo stack
    undo_top = push(undo_stack, undo_top, document)

    # Pop from redo stack
    document, redo_top = pop(redo_stack, redo_top)
    print("Redo performed.")


# ------------------ DISPLAY ----------------
def display_document():
    print("\nCurrent Document State:")
    print("-----------------------")
    if document == "":
        print("[EMPTY DOCUMENT]")
    else:
        print(document)


# -------------------------------------------
# MENU SYSTEM
# -------------------------------------------
while True:
    print("\n-------- MENU --------")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        make_change()

    elif ch == 2:
        undo()

    elif ch == 3:
        redo()

    elif ch == 4:
        display_document()

    elif ch == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
