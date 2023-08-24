#NEW TODO USING IF ELSE STATEMENTS AND MORE EFFICIENT
while True:
    userInput = input("Type add,edit,show,complete,quit: ")

    if userInput.startswith("add"):
        action = userInput[4:]
        with open("todoBetter.txt","+a") as f:
            f.writelines(action+"\n")
    elif userInput.startswith("show"):
        with open("todoBetter.txt","r") as f:
                #Yeah i know the list comprehension is too much to handle eh
                for i,j in enumerate([i.strip("\n") for i in f.readlines()],start=1):
                    print(f"{i}.{j}")
    elif userInput.startswith("edit"):
        try:
            editTodo = userInput[4:]
            index = int(editTodo) - 1
            newTodo = input("Please type in new Todo:") +"\n"
            
            with open("todoBetter.txt","r") as read:
                old = read.readlines()
                
            with open("todoBetter.txt","w") as write:
                old[index] = newTodo
                write.writelines(old)
        except ValueError:
            print("Wrong input. It's supposed to be a number instead.")
            continue
    elif userInput.startswith("complete"):
        try:
            completeTodo = int(userInput.strip("complete "))
            with open("todoBetter.txt","r") as f:
                lisp = f.readlines()
            vartodo = lisp[completeTodo -1]
            lisp.pop(completeTodo-1)
            with open("todoBetter.txt","w") as f:
                f.writelines(lisp)
            print(f"{vartodo} was removed")
        except IndexError:
            print("Number given is not in Todo List!")
            continue
            
    elif userInput.startswith("quit"): 
        break
    else:
        print("Command invalid try again!")