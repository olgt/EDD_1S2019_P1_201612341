import curses
import random
from structures import snake_Node
from structures import snake_Structure
from curses import textpad

snakeFinalReport = snake_Structure()
score = 0

def create_GameField(screen):
    screenHeight, screenWidth = screen.getmaxyx()
    box = [[3, 3], [screenHeight - 3, screenWidth - 3]]

    textpad.rectangle(screen, box[0][0], box[0][1], box[1][0], box[1][1])
    return box


def create_food(snakeFinal, box):
    food = None
    snakeArray = snakeFinal.toArray()

    while food is None:
        food = [random.randint(box[0][0]+1, box[1][0]-1),
                random.randint(box[0][1]+1, box[1][1]-1)]

        if food in snakeArray:
            food = None

    return food

def create_Snake(screen, screenHeight, screenWidth):
#Time/Box Settings
    actuaScore = 0
    box = create_GameField(screen)
    screen.nodelay(1)
    screen.timeout(150)
    screen.addstr(3,0,'Score = ' + str(actuaScore))
#Creation of the snake with 3 units
    snakeFinal = snake_Structure()
    for i in range(3):
        y = screenHeight // 2
        x = screenWidth // 2 - i
        snakeFinal.addPoint(1, x, y)
        snakeFinal.drawNodes(screen, x, y)

    headOfSnake = snakeFinal.head
    bad = False

#Creates a point and prints it
    food = create_food(snakeFinal,box)
    screen.addstr(food[0], food[1], '+')

#Sets the direction of the snake
    snakeDirection = curses.KEY_RIGHT

    while 1:
        key = screen.getch()

        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
            snakeDirection = key

        if snakeDirection == curses.KEY_RIGHT:
            newHead = [snakeFinal.head.y, snakeFinal.head.x + 1]
        elif snakeDirection == curses.KEY_LEFT:
            newHead = [snakeFinal.head.y, snakeFinal.head.x - 1]
        elif snakeDirection == curses.KEY_UP:
            newHead = [snakeFinal.head.y - 1, snakeFinal.head.x]
        elif snakeDirection == curses.KEY_DOWN:
            newHead = [snakeFinal.head.y + 1, snakeFinal.head.x]

# Adds the newhead and prints it
        snakeFinal.addPointAndChangeHead(1, newHead[1], newHead[0])

#This checks if the snake went through a point
        if snakeFinal.head.x == food[1] and snakeFinal.head.y == food[0]:
            if bad is True:
                actuaScore -= 1
                snakeFinal.removePointAndEraseFromScreen(screen)
                snakeFinal.removePointAndEraseFromScreen(screen)
            elif bad is False:
                actuaScore += 1

            screen.addstr(3, 0, 'Score = ' + str(actuaScore))

#Creates a point and prints it
            food = create_food(snakeFinal, box)

            if random.random() > 0.75:
                screen.addstr(food[0], food[1], '*')
                bad = True
            else:
                screen.addstr(food[0], food[1], '+')
                bad = False

        else:
            # Removes the last item of the snake and prints a blank
            snakeFinal.removePointAndEraseFromScreen(screen)

        snakeFinal.drawNodes(screen, newHead[1], newHead[0])
        screen.refresh()
#hecks if game has been won
        if actuaScore == 5:
            break

    snakeFinal.createSnakeReport()
    snakeFinalReport = snakeFinal

"""        
#This checks if the snake goes against any walls or againts itself
        if(snake[0][0] in [box[0][0], box[1][0]] or
                snake[0][1] in [box[0][1], box[1][1]] or
                snake[0] in snake[1:]):
            message = "Game Over"
            screen.addstr(screenHeight // 2, screenWidth // 2, message)
            screen.nodelay(0)
            screen.getch()
            break
"""
