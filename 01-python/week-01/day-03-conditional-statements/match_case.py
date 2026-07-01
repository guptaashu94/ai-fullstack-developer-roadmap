day = input("Enter day: ").lower()

match day:
    case "monday":
        print("Start of work week")
    case "friday":
        print("Weekend is near")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Regular day")