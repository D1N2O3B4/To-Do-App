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
            
        case "show":
            with open("todo.txt","r") as f:
                for i,j in enumerate(f.readlines(),start=1):
                    print(f"{i}.{j.strip('n')}")
            
        case "complete":
            pass
        case "quit":
            quitOpt = False
        case _:
            print("Command entered invalid!!")