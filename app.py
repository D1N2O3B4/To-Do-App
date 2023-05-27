store = []

def add(params):
    store.append(params)
def show():
    for i in store.index():
        print(f"{i}")

        
def remove(params):
    store.remove(params)

operations = {
    "add":add,
    "show":show,
    'remove':remove
}

user_choice = input("Type add,show,remove or press enter to quit")

if operations[user_choice] != "":
    pass

else:
    pass