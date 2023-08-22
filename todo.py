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
            file = open("todo.txt","r")
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            file = open("todo.txt","w")
            file.writelines(todos)
            file.close
           

        case "edit":
            editTodo = input("Input Todo number to edit:\n")
            
        case "show":
            pass
        case "complete":
            pass
        case "quit":
            quitOpt = False
        case _:
            print("Command entered invalid!!")