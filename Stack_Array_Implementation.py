# Stack array implementation in Python
# No list functions at all used.

# Get size from user
size = int(input("Enter stack size"))

# Creating list
stack = [None]*size

# Top pointer
top = 0

def push(item):
    global top                                  # Access the top pointer
    
    if is_full():                               # Catching error
        print("Stack overflow error.")
    else:
        stack[top] = item                       # Adding to stack
        top += 1                                # Increment pointer by 1 to get new top

# Procedure named as to not get it confused with the pop function
def pop_Stack():
    global top                                  # Access the pointer

    if is_empty():                              # Catching error
        print("Stack underflow error")
        return None
    else:
        item = stack[top - 1]                   # Get the item at the top of the stack
                                                # top - 1 is used as the pointer points to where new items go
        top -= 1                                # Decrease top by 1 to get new top
        return item                             # Return what we just got

# The length is the top of the stack
def find_length():
    return top

# The stack is empty if the top is also the bottom
def is_empty():
    return top == 0

# The stack is full if the top reaches the length of the array
def is_full():
    return top == size

# Get the top of the stack
# top - 1 is used as the pointer points to where new items go
def peek():
    if is_empty():                              # Catching error
        return "No value to peek"
    else:
        return stack[top - 1]


# Getting user input as to what functions to do
while True:
    print("1 - Push")
    print("2 - Pop")
    print("3 - Get stack height")
    print("4 - Check if empty")
    print("5 - Check if full")
    print("6 - Peek")
    print("7 - Exit")
    userInput = input("Enter option")

    match userInput:
        case "1":
            add = input("What to push?")
            push(add)
        case "2":
            print("Popped item:", pop_Stack())
        case "3":
            print("Stack height:", find_length())
        case "4":
            if is_empty():
                print("The stack is empty")
            else:
                print("The stack is not empty")
        case "5":
            if is_full():
                print("The stack is full")
            else:
                print("The stack is not full")
        case "6":
            print("Peeked value:", peek())
        case "7":
            break
        case _:
            print("Input error - please try again")