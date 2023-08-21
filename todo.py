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
            pass
        case "edit":
            pass
        case "show":
            pass
        case "complete":
            pass
        case "quit":
            quitOpt = False
        case _:
            print("Command entered invalid!!")