import structures
import csv
import curses
from structures import playerNode

playerSelected = playerNode("New Player")


def create_Filled_User_Structure(loaded_user_array):
    users = loaded_user_array
    structure_Of_Users = structures.userSeletionList()

    for user in users:
        structure_Of_Users.add(user)

    print("Done")
    return structure_Of_Users

def print_Users(screen, user):
    screen.clear()
    height, width = screen.getmaxyx()
    screen.addstr(int(height//2), int(width/2 - 4), user)
    screen.addstr(int(height//2 + 1), int(width/2 - 14), "<- Press Enter to select ->")
    screen.refresh()

def cycleThroughUsers(screen, users):
    structure_Of_Users = create_Filled_User_Structure(users)
    node = structure_Of_Users.head
    user = node.playerName

    print_Users(screen, str(user))

    while 1:
        key = screen.getch()
        if key == curses.KEY_RIGHT:
            node = node.next
            user = node.playerName
        elif key == curses.KEY_LEFT:
            node = node.prev
            user = node.playerName
        elif key == curses.KEY_ENTER or key == 10:
            playerSelected = node
            return playerSelected

        print_Users(screen, str(user))
    screen.clear()




