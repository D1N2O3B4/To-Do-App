user_input = input("Type in any day of the week:\n").capitalize()

match user_input:
    case "Monday":
        print("Garfield hates Mondays")
    case "Tuesday":
        print("Tuesdays are ok")
    case "Wednesday":
        print("Middle week day wednesday")
    case "Thursday":
        print("Mokuyoubi is Thursday in Japanese")
    case "Friday":
        print("Kinyoubi is friday in Japanese")
    case "Saturday":
        print("This day is for fun")
    case "Sunday":
        print("Sunday is always sunny")
    