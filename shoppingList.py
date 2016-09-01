MENU_TEXT = ["R", "List required items", "C", "List completed items", "A", "Add new item",
             "M", "Mark an item as completed", "Q", "Quit"]

itemFile = open("items.csv", "r+")


def main():
    print("Shopping List 1.0 - by Luke West")
    rowCount = 0
    for row in itemFile:
        rowCount += 1
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
            fileLineList = itemMenu("r")
            print(fileLineList)
            print("Enter the number of an item to mark as completed")
            while True:
                try:
                    itemCompleteInput = int(input(">>>"))
                    while itemCompleteInput not in range(len(fileLineList[::2])):
                        print("Invalid item number")
                        itemCompleteInput = int(input(">>>"))
                    break
                except ValueError:
                    print("Invalid input; enter a number")
            itemFile.seek(fileLineList[itemCompleteInput * 2 + 1])
            itemComplete = itemFile.readline()
            print(itemComplete)


        elif menuInput == "Q":
            print("Thanks for using the shopping list")
            itemFile.close()


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
    itemFile.seek(0)
    rowCount = 0
    itemCount = 0
    for row in itemFile:
        rowCount += 1
        item = row.split(",")
        if item[3] == "{}\n".format(itemState):
            itemCount += 1
    itemFile.seek(0)
    i = 0
    itemList = []
    itemOrder = [0] * rowCount
    itemTotal = 0.0
    fileLine = 0
    fileLineList = [0] * itemCount * 2
    for row in itemFile:
        item = row.split(",")
        if item[3] == "{}\n".format(itemState):
            itemList.append(item)
            itemOrder[int(itemList[i][2]) - 1] = i
            itemTotal += float(itemList[i][1])
            fileLineList[i * 2] = int(itemList[i][2])
            fileLineList[i * 2 + 1] = fileLine
            i += 1
        fileLine += len(row)
    for x in range(i):
        print("{}. {:18}  $ {:.2f} ({})".format(x, itemList[itemOrder[x]][0], float(itemList[itemOrder[x]][1]),
                                                itemList[itemOrder[x]][2]))
    print("Total expected price for {} items: ${:.2f}".format(i, itemTotal))
    return fileLineList

main()
