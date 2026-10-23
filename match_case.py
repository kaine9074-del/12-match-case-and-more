#the good old if/elif/else
#if i have a number respresenting days of th eweek
#1-7 sun - sat respectivley

#write me a function called get_day_name_if_else(num)
# it will take a num and return the day name
def get_day_name_if_else(num):
    if num == 1:
        print("Sunday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print("Wensday")
    elif num == 5:
        print("Thursday")
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")
    else:
        print("Invalid number.")

#A match case statment is a alternitive to useing multiple if, elif and else statments
#it workds by comparing a value (the "match") against several possible patterns (the "cases")
#when match found, code runs
def get_day_name_match(num):
    match num: 
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wensday")
        case 5:
            print("Thirsday")
        case 6:
            print("Friday")
        case 7:
            print("Sadurday")
        case _:
            print("Not avalid day")


get_day_name_match(1)
get_day_name_match(9)

def is_weekend(daystr:str) -> bool:
    match daystr:
        case "Sunday":
            return True
        case "Saturday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wensday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case _:
            return False


def is_weekend_shorter_match(daystr:str) -> bool:
    match daystr:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednsday" | "Thirsday" | "Friday":
            return False
        case _:
            raise ValueError(f"{daystr} is not a day, stupid!")
        
print(is_weekend("Sunday"))
print(is_weekend("Monday"))
print(is_weekend_shorter_match("Sunday"))
print(is_weekend_shorter_match("Monday"))
print(is_weekend_shorter_match(":)"))