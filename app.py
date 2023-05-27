store = []

def add(params):
    store.append(params)
def show():
    print(store)

        
def remove(params):
    store.remove(params)

operations = {
    "add":add,
    "show":show,
    'remove':remove
}

user_choice = input("Type add,show,remove or press enter to quit")

while operations[user_choice] != "":
    if user_choice == "add":
        action = input("Type in action")
        operations[user_choice](action)
        user_choice = input("Type add,show,remove or press enter to quit")
    else:
        operations[user_choice]