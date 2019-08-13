
import curses
from structures import scoreBoardLinkedList
from structures import scoreBoardNode

def scoreboardVisualization(screen, scoreboard):
    screen.clear()
    # Gets the perfect item/space height ratio
    height, width = screen.getmaxyx()

    temp = scoreboard.head
    i = 2
    screen.addstr(1, width // 2, "SCOREBOARD")
    #screen.addstr(1 + i, width // 2, str(temp.playerName) + '  ' + str(temp.score) + ' Points')

    while temp is not None and i < 10:
        screen.addstr(1 + i, width // 2, str(temp.playerName) + '  ' + str(temp.score) + ' Points')
        temp = temp.next
        i += 1
        screen.refresh()

    while 1:
        key = screen.getch()
        if key == curses.KEY_ENTER or key == 10:
            break
