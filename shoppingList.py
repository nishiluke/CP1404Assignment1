MENU_TEXT = ["R", "List required items", "C", "List completed items", "A", "Add new item",
             "M", "Mark an item as completed", "Q", "Quit"]

itemFile = open("items.csv", "r+")
rowCount = 0
itemList = []
for row in itemFile:
    itemList.append(row)
    rowCount += 1


def main():
    print("Shopping List 1.0 - by Luke West")
    print("{} items loaded from items.csv".format(rowCount))

    menuInput = ""
    while menuInput != "Q":
        menuInput = mainMenu()
        if menuInput == "R":
            print("Required items:")
            itemMenu("r")

        elif menuInput == "C":
            print("Completed items:")
            itemMenu("c")

        elif menuInput == "A":
            print("A")

        elif menuInput == "M":
            itemOrder = itemMenu("r")
            print("Enter the number of an item to mark as completed")
            while True:
                try:
                    itemMarkInput = int(input(">>>"))
                    while itemMarkInput not in range(len(itemOrder)):
                        print("Invalid item number")
                        itemMarkInput = int(input(">>>"))
                    break
                except ValueError:
                    print("Invalid input; enter a number")
            itemSelected = itemOrder[itemMarkInput]
            for row in itemList:
                if row == itemSelected:
                    row.replace("r\n", "c\n")
            print("{} marked as completed".format(itemSelected.split(",")[0]))
            print(itemList)
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


def itemMenu(itemState):
    itemCount = 0
    for row in itemList:
        item = row.split(",")
        if item[3] == "{}\n".format(itemState):
            itemCount += 1
    i = 0
    itemTotal = 0.0
    itemOrder = [0] * itemCount
    for priority in range(3):
        for row in itemList:
            item = row.split(",")
            if item[3] == "{}\n".format(itemState) and item[2] == str(priority + 1):
                print("{}. {:18}  $ {:.2f} ({})".format(i, item[0], float(item[1]),item[2]))
                itemTotal += float(item[1])
                itemOrder[i] = row
                i += 1
    print("Total expected price for {} items: ${:.2f}".format(i, itemTotal))
    return itemOrder

main()
