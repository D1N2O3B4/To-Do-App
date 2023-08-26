store = []

def add(params):
    store.append(params)

def show():
    index = 0
    for index,action in enumerate(store,start=1):
        print(f"{index}.{action}")

        
def remove(params):
    store.remove(params)


user_choice = input("Type add,show,remove or press enter to quit\n")

while user_choice != "":
    if user_choice == "add":
        action = input("Type in action\n")
        add(action)
        user_choice = input("Type add,show,remove or press enter to quit\n")
     
    else:
        if user_choice == "show":
            show()
            user_choice = input("Type add,show,remove or press enter to quit\n")
       
        else:
            action = input("Type in action to remove\n")
            remove(action)
            user_choice = input("Type add,show,remove or press enter to quit\n")
   
title = input("Type in title")

print(len(title.replace(" ","")))