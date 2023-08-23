quitOpt = True
while quitOpt:
    userChoice = input("""
                        Welcome to this simple Todo Script
                        To add a new Todo type \"add\"
                        To edit a Todo type \"edit\"
                        To show all Todos type \"show\"
                        To complete Todo type \"complete\"
                        To quit type \"quit\"
                        """)
    
    match(userChoice):
        case "add":
            todo = input("Enter a todo:\n")+"\n"
            with open("todo.txt","+a") as f:
                f.writelines(todo)
        case "edit":
            editTodo = input("Input Todo number to edit:\n")
            index = int(editTodo) - 1
            newTodo = input("Please type in new Todo:") +"\n"
        
            with open("todo.txt","r") as read:
                old = read.readlines()
            
            with open("todo.txt","w") as write:
                old[index] = newTodo
                write.writelines(old)
            
        case "show":
            with open("todo.txt","r") as f:
                #Yeah i know the list comprehension is too much to handle eh
                for i,j in enumerate([i.strip("\n") for i in f.readlines()],start=1):
                    print(f"{i}.{j}")
            
        case "complete":
            completeTodo = int(input("Input Todo number to complete:\n"))
            with open("todo.txt","r") as f:
                lisp = f.readlines()
            vartodo = lisp[completeTodo -1]
            lisp.pop(completeTodo-1)
            with open("todo.txt","w") as f:
                f.writelines(lisp)
            print(f"{vartodo} was removed")
        case "quit":
            quitOpt = False
        case _:
            print("Command entered invalid!!")