user_input = input("Type in any day of the week:\n").capitalize()

match user_input:
    case "Monday"| "Manday":
        print("Garfield hates Mondays. Fun fact i used to spell Monday Manday")
    case "Tuesday":
        print("Tuesdays are ok")
    case "Wednesday":
        print("Middle week day wednesday")
    case "Thursday":
        print("Mokuyoubi is Thursday in Japanese")
    case "Friday" | "Fryday":
        print("Kinyoubi is friday in Japanese. Fun fact i used to spell Friday Fryday")
    case "Saturday":
        print("This day is for fun")
    case "Sunday":
        print("Sunday is always sunny")
    #This gets called if no case matches your input any var or approved char can be used. eg: name,_name,defk etc
    case _:
        print("Your input doesn't match any case")
    