
from PIL import Image
import turtle 
import random
import time 

grid_size = 4
box_size = 100
candy_name = ["bluecandy.gif", "greencandy.gif", "purplecandy.gif", "redcandy.gif"]

box = "black"
time_of_box = 0
location = []
hold_candy = []
grid_candy = []
score = 0
click_candy = []
wanted_candy = ''
level = 1
candy_find = 4  

turtle_text = turtle.Turtle()
turtle_text.hideturtle()
turtle_text.penup()

def screen_setup():
    screen = turtle.Screen()
    screen.setup(width=800, height=800) 
    screen.title("Hide the Candy")
    screen.bgcolor("white")

    for candy in candy_name:
        screen.addshape(candy)

    return screen

def make_grid():
    center_x = -box_size * (grid_size // 2)
    center_y = box_size * (grid_size // 2)

    places = []

    for x in range(grid_size):
        for y in range(grid_size):
            position_x = center_x + (y * box_size)
            position_y = center_y - (x * box_size)
            position = (position_x, position_y)
            places.append(position)

    return places

def candy_turtle():
    turtles = []
    for i in range(grid_size * grid_size):
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        turtles.append(t)

    return turtles

def random_candylocation():
    global grid_candy
    grid_candy = []
    all_candies = candy_name * 4
    random.shuffle(all_candies)
    grid_candy = all_candies[:16]  

def make_candy():
    for i in range(len(hold_candy)):
        t = hold_candy[i]
        candy_locations = location[i]
        candy = grid_candy[i]
        t.goto(candy_locations)
        t.shape(candy)
        t.showturtle()

black_turtles = []

def black_box():
    global black_turtles, box_turtle
    #black_turtles = []

    for i in location:
        box_turtle = turtle.Turtle()
        box_turtle.penup()
        box_turtle.hideturtle()
        box_turtle.color(box)
        box_turtle.shape("square")
        box_turtle.shapesize(4.5, 4.5)  
        box_turtle.goto(i)
        box_turtle.showturtle()
        black_turtles.append(box_turtle)



def clear_box():
    global black_turtles

    for box_turtle in black_turtles:
        box_turtle.hideturtle()





def level_up():
    turtle_text.goto(0, 100)
    turtle_text.color('green')
    turtle_text.write(f"LEVEL {level} UP!", align="center", font=("Arial", 24, "bold"))
    time.sleep(1)
    turtle_text.clear()

    clear_box()

def start_game():
    global click_candy, wanted_candy, candy_find
    click_candy = []
    candy_index = random.randint(0, len(candy_name)-1)
    wanted_candy = candy_name[candy_index]
    game_score()
    
    make_candy()
    screen.update()
    time.sleep(2)  
    black_box()

def game_score():
    turtle_text.goto(0, 300)
    turtle_text.color('black')
    turtle_text.clear()
    turtle_text.write(f"Score: {score} Level: {level}", align="center", font=("Arial", 18, "bold"))
    turtle_text.goto(0, 270)
    turtle_text.write(f"Find all {wanted_candy.split('.')[0]}s!", align="center", font=("Arial", 18, "bold"))

def show_messages(message):
    turtle_text.goto(0, -250)
    turtle_text.clear()
    turtle_text.write(message, align="center", font=("Arial", 18, "bold"))

def screen_click(x, y):
    global score, click_candy, level, black_turtles
    
    for i in range(len(location)):
        position1 = location[i]
        if (position1[0] - box_size/2 < x < position1[0] + box_size/2 and 
            position1[1] - box_size/2 < y < position1[1] + box_size/2):
            if i not in click_candy:
                click_candy.append(i)
                if grid_candy[i] == wanted_candy:
                    show_messages('Correct!')
                    black_turtles[i].hideturtle()

                    
                    
                 
                    flag = True
                    for j in range(len(grid_candy)):
                        if grid_candy[j] == wanted_candy and j not in click_candy:
                            flag = False 
                    
                    if flag:
                        score += 1
                        show_messages('You found all candies! Next round...')
                        clear_box()
                        black_turtles.clear()
                        make_candy()
                        screen.update()
                        time.sleep(2)

                        if score % 3 == 0:
                            level += 1
                            level_up()
                        start_game()
                else:
                    show_messages('Wrong candy! Try again...')
                    score = max(0, score - 1)
                    time.sleep(1)
                    random_candylocation()
                    make_candy()
                    start_game()
                game_score()


def begin_screen():
    screen.bgpic("background2.gif")
    start_button = turtle.Turtle()
    start_button.shape("square")
    start_button.color("green")
    start_button.shapesize(4,10)
    start_button.penup()
    start_button.goto(0, 100)

    turtle_text.goto(0, 200)
    turtle_text.write("Welcome to Find The Candy!", align= "center", font=("Arial", 26, "bold"))
    turtle_text.goto(0, 100)
    turtle_text.write("Start", align="center", font=("Arial", 25, "bold"))

    screen.addshape(candy_name[3])
    moving_candy = turtle.Turtle()
    moving_candy.hideturtle()
    moving_candy.penup()
    moving_candy.shape(candy_name[3])
    start_position = [450, -50]
    end_position = [-450, -50]

    
    candy_moves(moving_candy, start_position, end_position)

    def click_start_button(x, y):
        global location, hold_candy
        if -80 < x < 80 and 80 < y < 120:
            start_button.hideturtle()
            turtle_text.clear()
            screen.bgpic("")
            moving_candy.hideturtle()
            screen.onclick(screen_click)
            location = make_grid()
            hold_candy = candy_turtle()
            random_candylocation()
            start_game()

    screen.onclick(click_start_button)

def candy_moves(candy_t, start, end):
    candy_t.goto(start[0], start[1])
    candy_t.showturtle()
    candy_t.speed(1)
    candy_t.goto(end[0], end[1])
    candy_t.goto(start[0], start[1])
screen = screen_setup()
begin_screen()
# location = make_grid()
# hold_candy = candy_turtle()
# random_candylocation()
# start_game()
# screen.onclick(screen_click)
screen.mainloop()


