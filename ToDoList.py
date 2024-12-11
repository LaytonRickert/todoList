"""
Name: Layton Rickert
Date: 12-10-24
Name of project: To make a list
Description: I will be making  a list while removing items from it
Class perioid: 1
"""
myList = ()
# varibles
toDoList =[]
# file name
fName = "data.txt"

#functions
def add_item(item):
    # add an item to the to do list
    toDoList.append(item)
def remove_item(item):
    #make a list of the items in the list
    for c in range(0, len(myList)):
        print(str(c + 1) + ". " + myList[c])
    choice = input("Which item would you like to remove? ")
    if choice.isnumeric():
        choice = int(choice)
        if choice-1 >= 0 and choice-1 < len(myList):
            myList.pop(int(choice-1))
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")




def reset_list():
    toDoList.clear()
def print_list():
    print(toDoList)
def show_menu():
    print("Pick 1 to add item to list: ")
    print("Pick 2 to remove item from to do list: ")
    print("Pick 3 to print the to do list: ")
    print("Pick 4 to reset the to do list: ")
    print("Pick 5 to quit: ")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_item("item")

    elif choice == "2":
        remove_item("item")

    elif choice == "3":
        print_list()
    elif choice == "4":
        reset_list()
    elif choice == "5":
        quit
    else:
        print("Invalid choice")

#testing remove when finished
print(toDoList)
show_menu()