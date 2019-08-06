import structures
import csv
import curses

def load_user_array():
    users = []
    with open('Usuarios.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif line_count is not 0:
                users.append(row)
                line_count +=  1
    #Imprime el numero de rows analizadas
    print(f'Processed {line_count} lines.')
    return users

def create_Filled_User_Structure():
    users = load_user_array()
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

def cycleThroughUsers(screen):
    structure_Of_Users = create_Filled_User_Structure()
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
        elif key == curses.KEY_LEFT or key == 10:
            break

        print_Users(screen, str(user))
    screen.clear()




