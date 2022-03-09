import turtle
import random

def Play_Again():
    global snake, snake_direction, food_pos, pen
    snake = [[0, 0], [0, 20], [0, 40], [0, 50], [0, 60]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    Game()


width = 500
height = 500
DELAY = 100  
food_size = 10

offsets = {
    "up": (0, 20),"down": (0, -20),"left": (-20, 0),"right": (20, 0)
}

def Game():

    global snake_direction
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_direction][0]
    new_head[1] = snake[-1][1] + offsets[snake_direction][1]
    snake.append(new_head)
    if not food_collision():
        snake.pop(0)  

    if snake[-1][0] > width / 2:
        snake[-1][0] -= width
    elif snake[-1][0] < - width / 2:
        snake[-1][0] += width
    elif snake[-1][1] > height / 2:
        snake[-1][1] -= height
    elif snake[-1][1] < -height / 2:
        snake[-1][1] += height

    pen.clearstamps()

    for segment in snake:
        pen.goto(segment[0], segment[1])
        pen.stamp()

    screen.update()

    turtle.ontimer(Game, DELAY)

def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(- width / 2 + food_size, width / 2 - food_size)
    y = random.randint(- height / 2 + food_size, height / 2 - food_size)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# Screen
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("green")
screen.setup(500, 500)
screen.tracer(0)



# Food
food = turtle.Turtle()
food.color("red")
food.shape("circle")
food.shapesize(food_size / 20)  
food.penup()

# Pen
pen = turtle.Turtle("square")
pen.penup()

# Event handlers
screen.listen()
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_up, "Up")
screen.onkey(go_right, "Right")

Play_Again()
turtle.done()