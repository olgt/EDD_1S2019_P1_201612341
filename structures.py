
import os
import curses
import subprocess

#Node for players Structure
class playerNode:
        def __init__(self, playerName):
            self.playerName = playerName
            self.next = None
            self.prev = None

#Circular Double Linked List (uses the Node structure)
class userSeletionList:
    def __init__(self):
        self.head = None

    def add(self, user_name):
        if self.head is None:
            newPlayerNode = playerNode(user_name)
            newPlayerNode.prev = None
            self.head = newPlayerNode
        else:
            newPlayerNode = playerNode(user_name)
            head = self.head
            temp = self.head
            while temp.next and temp.next is not head:
                temp = temp.next
            temp.next = newPlayerNode
            newPlayerNode.next = head
            newPlayerNode.prev = temp
            self.head.prev = newPlayerNode

    # Generates double linked list
    def generate_graphviz(self):
        if self.head is None:
            print('The list is Empty')
        else:
            f = open('UsersReport.dot', 'w')
            f.write('digraph firstGraph{\n')
            f.write('node [shape = record];\n')
            f.write('rankdir=LR;\n')
            temp = self.head
            count = 0

            while temp.next is not None and temp.next is not self.head:
                f.write('node{} [label=\" {} \"];\n'.format(count, str(temp.playerName)))
                count += 1
                f.write('node{} -> node{};\n'.format(count - 1, count))
                f.write('node{} -> node{};\n'.format(count, count - 1))
                temp = temp.next

            # print(temp.id)
            f.write('node{} [label=" {} \"];\n'.format(count, str(temp.playerName)))
            f.write('node{} -> node{};\n'.format(count, 0))
            f.write('node{} -> node{};\n'.format(0, count))
            f.write('}')
            f.close()
            os.system('dot UsersReport.dot -Tpng -o UsersReport.png')
            try:
                os.startfile('UsersReport.png')
            except:
                print('Error')

#Node for score Structure
class pointNode:
    def __init__(self, x,y, value):
        self.head = None
        self.next = None
        self.x = x
        self.y = y
        self.value = value

#Stack linked list (Uses pointNode Structure)
class scoreList:
    def __init__(self):
        self.head = None

    def push(self, newNode): #Method to push a new node to stack
        if self.head is None:
            self.head = newNode
        else:
            head = self.head
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def pop(self): #Method to pop last entry
        temp = self.head
        tempBehind = self.head
        while temp.next is not None:
            tempBehind = temp
            temp = temp.next

        temp = None
        tempBehind.next = None

    def createPointsReport(self):
        if self.head is None:
            print('The list is Empty')
        else:
            f = open('PointsReport.dot', 'w')
            f.write('digraph firstGraph{\n')
            f.write('rankdir=BT;\n')
            f.write('node [shape = record];\n')
            #f.write('rankdir=LR;\n')
            temp = self.head
            count = 0
            f.write('hashTable [label=\"'.format(count, str(temp.x) + ',' + str(temp.y)))
            while temp.next is not None:
                f.write('<f{}>{}|'.format(count, str(temp.x) + ',' + str(temp.y)))
                count += 1
                temp = temp.next
#hashTable [label="<f0>0|<f1>1|<f2>2|<f3>3|<f4>4|<f5>5|<f6>6|<f7>7|<f8>8"];
            # print(temp.id)
            f.write('<f{}>{}|'.format(count + 1, str(temp.x) + ',' + str(temp.y)))
            f.write('<f{}> {}\"];\n'.format(count, " "))
            f.write('}')
            f.close()
            os.system('dot PointsReport.dot -Tpng -o PointsReport.png')
            try:
                os.startfile('PointsReport.png')
            except:
                print('Error')

#Node for scoreboard players/score
class scoreBoardNode:
    def __init__(self, playerName, score):
        self.playerName = playerName
        self.score = score
        self.next = None

#Queue Linked list (uses scoreBoardNode)
class scoreBoardLinkedList:
    def __init__(self):
        self.head = None

    def enqueue(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            head = self.head
            temp = self.head

            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def dequeue(self): #removes the first entry
        head = self.head
        temp = head.next
        head = None
        self.head = temp

    def createPointsReport(self):
        if self.head is None:
            print('The list is Empty')
        else:
            f = open('ScoreboardReport.dot', 'w')
            f.write('digraph firstGraph{\n')
            f.write('node [shape = record];\n')
            f.write('rankdir=LR;\n')
            temp = self.head
            count = 0

            while temp.next is not None:
                f.write('node{} [label=\" {} \"];\n'.format(count, temp.playerName + ', ' + str(temp.score)))
                count += 1
                f.write('node{} -> node{};\n'.format(count - 1, count))
                temp = temp.next

            # print(temp.id)
            f.write('node{} [label=\" {} \"];\n'.format(count,  temp.playerName + ', ' + str(temp.score)))
            count += 1
            f.write('node{} -> node{};\n'.format(count - 1, count))
            f.write('node{} [label=\" {} \"];\n'.format(count, " "))
            f.write('}')
            f.close()
            os.system('dot ScoreboardReport.dot -Tpng -o ScoreboardReport.png')
            try:
                os.startfile('ScoreboardReport.png')
            except:
                print('Error')

#Node for Snake
class snake_Node:
    def __init__(self, value, x, y):
        self.value = value
        self.y = y
        self.x = x
        self.head = None
        self.prev = None
        self.next = None

#Double Linked list for the Snake
class snake_Structure:
    def __init__(self):
        self.head = None

    def addPoint(self, value, x, y):
        newSnakeNode = snake_Node(value,x,y)
        if self.head is None:
            self.head = newSnakeNode
            newSnakeNode.next = None
            newSnakeNode.prev = None
        else:
            temp = self.head
            while temp.next and temp.next is not None:
                temp = temp.next
            newSnakeNode.prev = temp
            temp.next = newSnakeNode


    def addPointAndChangeHead(self, value, x, y):
        newSnakeNode = snake_Node(value, x, y)

        temp = self.head

        newSnakeNode.next = temp
        newSnakeNode.prev = None

        temp.prev = newSnakeNode

        self.head = newSnakeNode

    def removePointAndEraseFromScreen(self, screen):
        temp = self.head

        while temp.next:
            temp = temp.next
        screen.addstr(temp.y, temp.x, ' ')
        temp.prev.next = None
        temp = None

    def passingThroughPoint(self, character, x, y):
        snakePoint = snake_Node(character, x, y)

        if character is '+':
            self.addPoint(snakePoint)
        elif character is '*':
            self.removePoint()

    def drawNodes(self, screen, x, y):
        temp = self.head
        while temp.next:
            screen.addstr(temp.y, temp.x, '#')
            temp = temp.next

    def toArray(self):

        snakeArray = []
        temp = self.head


        while temp.next is not None:
            coordenatesNode = [temp.x, temp.y]
            snakeArray.append(coordenatesNode)
            temp = temp.next

        return snakeArray

    def checkIfSnakeCrashes(self, box):
        state = False
        temp = self.head.next

        while temp.next and temp.next is not None:
            if self.head.x is temp.x and self.head.y is temp.y:
                state = True
                return state
            temp = temp.next

        temp = self.head
        if self.head.y in [box[0][0], box[1][0]] or self.head.x in [box[0][1], box[1][1]]:
            state = True
            return state

        return state

    def createSnakeReport(self):
        if self.head is None:
            print('The list is Empty')
        else:
            f = open('SnakeReport.dot', 'w')
            f.write('digraph firstGraph{\n')
            f.write('node [shape = record];\n')
            f.write('rankdir=LR;\n')
            temp = self.head
            count = 1

            f.write('node{} [label=\" {} \"];\n'.format(count - 1, "NULL"))
            f.write('node{} -> node{};\n'.format(count, count - 1))

            while temp.next is not None:
                f.write('node{} [label=\" {} \"];\n'.format(count, str(temp.x) + ',' + str(temp.y)))
                count += 1
                f.write('node{} -> node{};\n'.format(count - 1, count))
                f.write('node{} -> node{};\n'.format(count, count - 1))
                temp = temp.next

            # print(temp.id)

            f.write('node{} [label=\" {} \"];\n'.format(count, str(temp.x) + ',' + str(temp.y)))
            f.write('node{} -> node{};\n'.format(count, count + 1))
            f.write('node{} [label=\" {} \"];\n'.format(count + 1, "NULL"))
            f.write('}')
            f.close()
            os.system('dot SnakeReport.dot -Tpng -o SnakeReport.png')
            try:
                os.startfile('SnakeReport.png')
            except:
                print('Error')

