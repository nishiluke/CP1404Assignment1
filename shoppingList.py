MENU_TEXT = ["R", "List required items", "C", "List completed items", "A", "Add new item",
             "M", "Mark an item as completed", "Q", "Quit"]


def main():
    itemList = open("items.csv", "r+")
    print("Shopping List 1.0 - by Luke West")
    rowCount = 0
    for row in itemList:
        rowCount += 1
    print("{} items loaded from items.csv".format(rowCount))

    menuInput = ""
    while menuInput != "Q":
        menuInput = mainMenu()
        if menuInput == "R":
            print("Required items:")
            itemList.seek(0)
            i = 0
            for row in itemList:
                item = row.split(",")
                if item[3] == "r\n":
                    print("{}. {:18}  $ {:.2f} ({})".format(i, item[0], float(item[1]), item[2]))
                    i += 1
        elif menuInput == "C":
            print("C")
        elif menuInput == "A":
            print("A")
        elif menuInput == "M":
            print("M")
        elif menuInput == "Q":
            print("Thanks for using the shopping list")

def mainMenu():
    userInput = ""
    while userInput not in MENU_TEXT[::2]:
        print("Menu:")
        for item in range(5):
            item *= 2
            print("{} - {}".format(MENU_TEXT[item], MENU_TEXT[item+1]))
        userInput = str(input(">>>")).upper()
        if userInput not in MENU_TEXT[::2]:
            print("Invalid menu choice")
    return userInput


main()
