
import curses
import menu_Option_1
import menu_Option_3
import menu_Option_5
from menu_Option_1 import create_Snake
from menu_Option_3 import cycleThroughUsers
from menu_Option_3 import create_Filled_User_Structure
from menu_Option_5 import print_Instructions
from menu_Option_5 import load_user_array
from menu_Option_4 import generatePlayerReport
from structures import playerNode, scoreBoardLinkedList, scoreBoardNode

#Global Variables
global actualScore
global actualUser
actualUser = playerNode("New Player")
actualScore = 0


users = []

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

def printReportsSubMenu(screen, selectedOption, optionFive, users, snakeForReport, yumsStructure, scoreBoardStructure):
#Settings/Prints menu
    screen.clear()
    menuOptions = ["Reports Menu", "1. Snake Report", "2.Score Report", "3. Scoreboard Report", "4. Users Report",
                   "Back"]
    # Gets the perfect item/space height ratio
    height, width = screen.getmaxyx()

    # Prints all the options to the menu centered
    for index, option in enumerate(menuOptions):
        x = (width // 2) - (len(menuOptions[index]) // 2)
        y = (height // 2) - (len(menuOptions) // 2) + index
        if (
                index == selectedOption):  # If the selection number is the same as in the option number, print with color
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, menuOptions[index])
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y, x, menuOptions[index])

    while 1:
        screen.addstr(5,5, str(selectedOption))

        key = screen.getch()

#Sets the Limit for the menu
        if key == curses.KEY_UP and selectedOption > 1:
            selectedOption -= 1
        elif key == curses.KEY_DOWN and selectedOption < 5:
            selectedOption += 1

#Option 1 Snake Report
        if key == curses.KEY_ENTER or key == 10 and selectedOption == 1:
            snakeForReport.createSnakeReport()
            pass
#Option 2 Score Report
        elif key == curses.KEY_ENTER or key == 10 and selectedOption == 2:
            yumsStructure.createPointsReport()
            pass

#Option 3 ScoreBoard Report
        elif key == curses.KEY_ENTER or key == 10 and selectedOption == 3:
            scoreBoardStructure.createPointsReport()
            pass
#Option 4 Users Report
        elif key == curses.KEY_ENTER or key == 10 and selectedOption is 4:
            if (optionFive):
                usersStructure = create_Filled_User_Structure(users)
                generatePlayerReport(usersStructure)
            elif (optionFive is False):
                screen.addstr(5, 5, "No Users Loaded")

        #Go Back to Main Menu
        elif key == curses.KEY_ENTER or key == 10 and selectedOption == 5:
            break

        printReportsSubMenu(screen,selectedOption, optionFive, users, snakeForReport, yumsStructure, scoreBoardStructure)
        screen.addstr(5,5, str(selectedOption))
        break

def getNewName(screen):
    curses.echo()
    curses.curs_set(True)
    screen.addstr(5, 5, "No Users Loaded. Please write the name of the player: ")
    nameOfPlayer = screen.getstr()
    actualUser = playerNode(nameOfPlayer)
    curses.curs_set(False)
    screen.clear()
    return actualUser

def main(screen):
    curses.curs_set(0) #Sets the blinking off
    selectedOptionIndex = 1 #This is the first option that the selection is at
    isOptionFivePressed = False
    height, width = screen.getmaxyx()
    printMenu(screen, selectedOptionIndex)

#This is used to count less than 10 games
    gamesForScoreBoardCounter = 0
    scoreBoard = scoreBoardLinkedList()
    actualUser = playerNode("New Player")

    while 1:
        key = screen.getch()
        screen.clear()
#Sets the limits so that you won't go further than the options
        if key == curses.KEY_UP and selectedOptionIndex > 1:
            selectedOptionIndex -= 1
        elif key == curses.KEY_DOWN and selectedOptionIndex < 6:
            selectedOptionIndex += 1
        elif selectedOptionIndex == 0 or selectedOptionIndex > 6:
            selectedOptionIndex = 1
            printMenu(screen, selectedOptionIndex)
#Option 1
        elif key == curses.KEY_ENTER or key == 10 and selectedOptionIndex == 1:
            if(isOptionFivePressed):
                snakeForReport, actualScore, yumsStructure = create_Snake(screen, height,width)

            elif(isOptionFivePressed is False):
                actualUser = getNewName(screen)
                create_Snake(screen, height, width)

    #Here we add the players to the ScoreBoard Structure and if it goes over 10, eliminate the head (FIFO)
            playerWithScoreNode = scoreBoardNode(str(actualUser.playerName), actualScore)
            scoreBoard.enqueue(playerWithScoreNode)
            gamesForScoreBoardCounter += 1
            if gamesForScoreBoardCounter is 10:
                scoreBoard.dequeue()
                gamesForScoreBoardCounter -= 1

#Option 3 Choose User
        elif key == curses.KEY_ENTER or key == 10 and selectedOptionIndex == 3:
            if(isOptionFivePressed is False):
                print("No Users have been added")
            else:
                actualUser = cycleThroughUsers(screen, users)
                print("User Selected = " + str(actualUser.playerName))
#Option 4 Reports
        elif key == curses.KEY_ENTER or key == 10 and selectedOptionIndex == 4:
            printReportsSubMenu(screen, 0, isOptionFivePressed, users, snakeForReport, yumsStructure, scoreBoard)
            screen.clear()
#Option 5 Load Users
        elif key == curses.KEY_ENTER or key == 10 and selectedOptionIndex == 5:
            print_Instructions(screen)
            users = load_user_array()
            isOptionFivePressed = True
            screen.clear()
#Exit
        elif key == curses.KEY_ENTER or key == 10 and selectedOptionIndex == 6:
            break

        printMenu(screen,selectedOptionIndex)
        screen.refresh()

#Initializatin Curses Library Window | Wraps main
curses.wrapper(main)