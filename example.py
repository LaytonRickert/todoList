# myList is a global variable that holds the to do items
# it is a list and the items are strings
myList = ("Red", "Orange", "Green", "yellow")

def have_fun():
    pass
def save_file():
    #do this when you quit the program
     with open(fName, "w") as f:
         file.writelines(item + "\n"" for item in myList)
     pass
def load_file():
    #do this when you start the program
    with open(fName, "r") as file:
        myList = [line.strip() for line in file]
def show_menu():
    """This is  a docString and it can be
    multiline
    The show_menu function has no parameter and returns
    nothing. It is used as the entry point to the to do list program and displays a menu"""
    while True:
        print("Pick 1 have fun")
        print("Pick 2 to do work")
        print("Pick 3 to quit")
        # choice holds the input choice from the menu
        choice = input("Enter your choice: ")
        if choice == "1":
        have_fun()
    elif choice == "2":
    #do something
    pass
elif choice == "3":
print("bye!!")
break
else:
print("Invalid choice")


def remove_Something():
    # make a list of the items in the list
    for c in range(0, len(myList)):
        print(str(c + 1)+ ". " + myList[c])
    choice = input("Which one do you want to remove?: ")
    if choice.isnumeric():
        choice = int(choice)
        if choice-1 >= 0 and choice-1 < len(myList):
            myList.pop(int(choice - 1))
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")

#This is how you make a list
print(myList)
remove_Something()
print(myList)

# This is how you make a list
myList = ["thing 1", "thing 2", "thing 3"]
#This is how you access individual  in the list
print(myList(1))item
print(myList(3))
#This is how you add to the end of the list
myList.append("thing 5")
#This is how you print the entire list
print(myList)
#This is how you remove an item using the index
myList.pop(2)
print(myList)
show_menu()
load_file()