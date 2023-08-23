while True:
    userInput = input("Type add,edit,show,complete,quit: ")

    if "add" in userInput:
        action = userInput.strip("add ")
        with open("todoBetter.txt","+a") as f:
            f.writelines(action+"\n")
    elif "show" in userInput:
        with open("todoBetter.txt","r") as f:
                #Yeah i know the list comprehension is too much to handle eh
                for i,j in enumerate([i.strip("\n") for i in f.readlines()],start=1):
                    print(f"{i}.{j}")
    elif "edit" in userInput:
        editTodo = userInput.strip("edit ")
        index = int(editTodo) - 1
        newTodo = input("Please type in new Todo:") +"\n"
        
        with open("todoBetter.txt","r") as read:
            old = read.readlines()
            
        with open("todoBetter.txt","w") as write:
            old[index] = newTodo
            write.writelines(old)
    elif "complete" in userInput:
        completeTodo = int(userInput.strip("complete "))
        with open("todoBetter.txt","r") as f:
            lisp = f.readlines()
        vartodo = lisp[completeTodo -1]
        lisp.pop(completeTodo-1)
        with open("todoBetter.txt","w") as f:
            f.writelines(lisp)
        print(f"{vartodo} was removed")
            
    elif "quit" in userInput: 
        break
    else:
        print("Command invalid try again!")