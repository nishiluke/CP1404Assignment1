import os

MENU_TEXT = ["R", "List required items", "C", "List completed items", "A", "Add new item",
             "M", "Mark an item as completed", "Q", "Quit"]


def main():
    itemList = open("items.csv", "w+")
    print("Shopping List 1.0 - by Luke West")
    rowCount = 0
    for row in itemList:
        rowCount += row
    print("{} items loaded from items.csv".format(rowCount))
    menuInput = mainMenu()


def mainMenu():
    output = ""
    while output not in MENU_TEXT[::2]:
        print("Menu:")
        for item in range(5):
            item *= 2
            print("{} - {}".format(MENU_TEXT[item], MENU_TEXT[item+1]))
        output = str(input(">>>")).upper
        if output not in MENU_TEXT[::2]:
            print("Invalid menu choice")
            print(MENU_TEXT[::2])
    return output.lower


main()
