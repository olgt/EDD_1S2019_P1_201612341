import curses
import random
from structures import snake_Node
from structures import snake_Structure
from curses import textpad

snakeFinal = snake_Structure()

def create_GameField(screen):
    screenHeight, screenWidth = screen.getmaxyx()
    box = [[3, 3], [screenHeight - 3, screenWidth - 3]]

    textpad.rectangle(screen, box[0][0], box[0][1], box[1][0], box[1][1])
    return box


def create_food(snake, box):
    food = None

    while food is None:
        food = [random.randint(box[0][0]+1, box[1][0]-1),
                random.randint(box[0][1]+1, box[1][1]-1)]

        if food in snake:
            food = None

    return food

def create_Snake(screen, screenHeight, screenWidth):
#Time/Box Settings
    box = create_GameField(screen)
    screen.nodelay(1)
    screen.timeout(150)
#Creation of the snake with 3 units
    for i in range(3):
        y = screenHeight // 2
        x = screenWidth // 2 - i
        snakeFinal.addPoint(1, x, y)
        snakeFinal.drawNodes(screen, x, y)

    headOfSnake = snakeFinal.head
    snakeDirection = curses.KEY_RIGHT

#Creates a point and prints it
    """food = create_food(snake,box)
    screen.addstr(food[0], food[1], '+')"""

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
        snakeFinal.removePoint()
        snakeFinal.drawNodes(screen, newHead[1], newHead[0])

"""
#This checks if the snake went through a point
        if snake[0] == food:
            # Creates a point and prints it
            food = create_food(snake, box)
            screen.addstr(food[0], food[1], '+')
        else:
            # Removes the last item of the snake and prints a blank
            screen.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

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
