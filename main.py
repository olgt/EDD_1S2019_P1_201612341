
import curses
import menu_Option_3
import menu_Option_5
from menu_Option_3 import cycleThroughUsers
from menu_Option_5 import print_Instructions

def printMenu(screen, selectedOptionIndex):
    menuOptions = ["Main Menu", "1. Play", "2. Scoreboard", "3. User Selection",
                   "4. Reports", "5. Bulk Loading", "6. Exit"]

    # Gets the perfect item/space height ratio
    height, width = screen.getmaxyx()

    #sets the color template
    curses.init_pair(1,curses.COLOR_WHITE, curses.COLOR_GREEN)
    # Prints all the options to the menu centered
    for index, option in enumerate(menuOptions):
        x = (width // 2) - (len(menuOptions[index]) // 2)
        y = (height // 2) - (len(menuOptions) // 2) + index
        if(index == selectedOptionIndex): #If the selection number is the same as in the option number, print with color
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, menuOptions[index])
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y, x, menuOptions[index])

def main(screen):
    curses.curs_set(0) #Sets the blinking off
    selectedOptionIndex = 0 #This is the first option that the selection is at

    printMenu(screen, selectedOptionIndex)

    while 1:
        key = screen.getch()
        screen.clear()

        if key == curses.KEY_UP and selectedOptionIndex > 0:
            selectedOptionIndex -= 1
        elif key == curses.KEY_DOWN and selectedOptionIndex < 7:
            selectedOptionIndex += 1
        elif selectedOptionIndex < 0 or selectedOptionIndex >= 6:
            selectedOptionIndex = 0
            printMenu(screen, selectedOptionIndex)
        elif key == curses.KEY_ENTER or key == 10 and selectedOptionIndex == 3:
            cycleThroughUsers(screen)
        elif key == curses.KEY_LEFT:
            break
        elif key == curses.KEY_ENTER or key == 10 and selectedOptionIndex == 5:
            print_Instructions(screen)
            screen.clear()

        printMenu(screen,selectedOptionIndex)
        screen.refresh()

#Initializatin Curses Library Window | Wraps main
curses.wrapper(main)