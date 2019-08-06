
import curses

def print_Instructions(screen):
    screen.clear()
    height, width = screen.getmaxyx()

    instructions = """               1. Create a csv file 
                    2. Save the file under the directory of this folder
                    3. Go to the game menu and press the option 5
                    4. Done.
                    Note: If you are reading while doing the instructions, go back to the menu and press option 5 again."""
    screen.addstr(int(height//2), int(width/2 - 4), "Instructions to add players via file")
    screen.addstr(2, 3, instructions)
    screen.refresh()

    key = screen.getch()
    while 1:
        if(key == curses.KEY_ENTER or key == 10):
            break

    print("Operation Successful")