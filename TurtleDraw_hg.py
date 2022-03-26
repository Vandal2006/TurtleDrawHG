#turtle Draw
#By: Henry Gilson
import turtle

success = False
while success == False:
    try:
        FILENAME = input('\nEnter file name')
        FILE = open(FILENAME,'r')
        success = True
    except Exception as e:
        print('File not found')

turtle.screensize(450,450)
hank = turtle.Turtle()
hank.speed(0)
hank.penup()

DISTANCE = []

print('Hank is drawing your picture now')
for line in FILE:
    parts = line.split(' ')
    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        
        hank.color(color)
        hank.goto(x,y)
        hank.pendown()
        DISTANCE.append(turtle.distance(x,y))
    else:
        hank.penup()

FILE.close()
TOTAL = sum(DISTANCE)
hank.penup()
hank.goto(100,-100)
hank.color('black')
hank.pendown()
hank.write('Total distance drawn is %.2f' %TOTAL, False, 'left',('Times New Roman',10,'normal'))
print('\nThe total distance of the line is: %.2f' % TOTAL)

input=input('\n\nPress Enter to close')

turtle.bye()

print('\nEnd')