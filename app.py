user_choice = input("Type add,show,remove or press enter to quit")
store = []

def add(params):
    store.append(params)

    
def show():
    for i in store.index():
        print(f"{i}")


def remove(params):
    store.remove(params)

