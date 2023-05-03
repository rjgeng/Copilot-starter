from multiprocessing import parent_process
import turtle
import time
import random
from racing_turtle import *
from playground import *

color_scheme = [
    # order = board, background, 7tiles, screen background, text color

    # the classic board, just the way everybody loves the blocks to be like
    ['black','lightblue', 'yellow', 'orange', 'green', 'purple', 'blue', 'red', 'wheat', 'black'],
    # a glacial color designed to hurt your eyes
    ['snow', 'cornflower blue', 'royal blue', 'powder blue', 'sky blue', 'steel blue', 'light blue', 'deep sky blue', 'alice blue', 'navy'],
    # the peacock color design, blue green, and a tiny bit of light orange
    ['azure', 'light sea green', 'cadet blue', 'coral','gold','medium aquamarine','cornflower blue', 'turquoise','light slate gray', 'aquamarine'],
    # some of our favorite food, now in turtle colors
    ['antique white', 'salmon', 'light salmon', 'dark salmon', 'tomato', 'coral', 'orange red', 'chocolate', 'cornsilk', 'maroon']]

# each time a new window opens, select a random set of presets colors from color scheme 
seed = random.randint(0, len(color_scheme) - 1)
colors = color_scheme[seed]

# render the GUI window
ws = turtle.Screen()
ws.title("CS10 Final Project")
bgcolor = colors[8]
ws.bgcolor(bgcolor)
ws.setup(width=1200, height=800)
ws.tracer(0)

init_x = -500
init_y = -600
init_pos = (init_x, init_y)

x_spawn = -400
y_spawn = -200

# other global variables 
score = 0
gameover = False

# instantiate a new turtle pen for rendering
tp = turtle.Turtle()
tp.penup()
tp.shape('turtle')
tp.speed('fastest')

# lists of available keys in each scene
main_keys = ['s', 't', 'd', 'q']
return_keys = ['b']
difficulty_keys = ['1', '2', '3', '4', 'f']
game_keys = ['Up', 'Down', 'Left', 'Right', 'z', 'c', 'space']
total_t_keys = main_keys + return_keys + difficulty_keys


# create the shape for the start of the game
tortoise = None # the current tortoise
num = random.randint(1, 7)
print(f'random.randint(1, 7): {num}')
tortoise_next = tortoise_factory(Tortoise.Types(num)) # the next tortoise
tortoise_pos = (x_spawn, y_spawn) # position of the current tortoise 

def render_playground(playground, tp):
    """
    Renders the playground with all the blocks. 
    """
    try: 
        tp.clear()

    except Exception as err:
        pass
    
def render_tortoise(tortoise, tp, tortoise_pos):
    """ Render a tortoise in or out of the playground. """
    pos_color = colors[tortoise.get_index()]
    tp.color(pos_color)
    pos_x, pos_y = tortoise_pos
    tp.goto(pos_x, pos_y)
    print(f'pos_x, pos_y: {pos_x, pos_y}')
    tp.stamp()

def render_score(tp, score):
    """ Render the player's current score, the holder, and the next tortoise ng a game. """
    font_size = 20
    font_set = ("Arial", font_size, "normal")
    tp.color(colors[9])
    tp.hideturtle()
    tp.goto(50, 300)
    tp.write("Score: {}".format(score), move=False, align="left", font=font_set)
    tp.goto(-160, 200)
    tp.write("Holder:", move=False, align="left", font=font_set)
    tp.goto(20, 200)
    tp.write("Next:", move=False, align="left", font=font_set)

   
def play_game():
    tp.clear()
    align_str = 'left'
    font_setting = ("Cambria", 15, "normal")
    x_p = -200
    
    tortoises = []
    
    global tortoise_pos    
    for i in range(6):
        num = random.randint(1, 7)
        print(f'random.randint(1, 7): {num}')
        tortoise_next = tortoise_factory(Tortoise.Types(num)) # the next tortoise
        new_tortoise = render_tortoise(tortoise_next, tp, tortoise_pos)
        tortoises.append(new_tortoise)
        tortoise_pos =  tortoise_pos[0], tortoise_pos[1] + 40
        

    for tor in tortoises:
        print(tor)
        # tor.forward(random.randint(1, 20))
        # if tor.xcor() > 250:
        #     tor.write("I won", font=("Arial", 33, "bold"))
        #     finish = True
        #     break

     
    render_score(tp, score)
    tp.goto((x_p, -300))
    tp.write('Press (b) to go back to the main menu. ', move=False, align=align_str, font=("Cambria", 16, "italic"))
    turtle.listen() 
    turtle.onkey(display_main_menu, 'b')

def game_over():
    deactivate_all_keys()
    tp.clear()
    tp.goto((0, 0))
    tp.write('GAME OVER!', move=False, align="center", font=("Arial", 32, "normal"))
    tp.goto((0, -50))
    tp.write('Press (b) to return to main menu.', move=False, align="center", font=("Arial", 15, "italic"))
    turtle.listen()
    turtle.onkey(display_main_menu, 'b')
    ws.mainloop()
    tp.hideturtle()

def view_tutorial():
    deactivate_all_keys()
    tp.clear()
    align_str = 'left'
    font_setting = ("Cambria", 15, "normal")
    x_p = -200
    tp.goto((x_p, 200))
    tp.write('(key) - function', move=False, align=align_str, font=("Cambria", 15, "bold"))
    tp.goto((x_p, 150))
    tp.write('(space) - hard-drop the tortoise. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, -50))
    tp.write('(left) - left-shift the tortoise. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, -100))
    tp.write('(right) - right-shift the tortoise. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, -150))
    tp.write('(c) - put the tortoise in hold. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, -200))
    tp.write('Note:', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, -240))
    tp.write('as the game proceeds. ', move=False, align=align_str, font=font_setting)
    tp.goto((x_p, -300))
    tp.write('Press (b) to go back to the main menu. ', move=False, align=align_str, font=("Cambria", 16, "italic"))
    turtle.listen() 
    turtle.onkey(display_main_menu, 'b')
    ws.mainloop()


def return_main_from_d():
    deactivate_all_keys()
    for t in level_turtle_lst:
        t.clear()
        t.penup()
        t.hideturtle()
    display_main_menu()

def quit_game():
    try: 
        ws.bye()
    except Exception as err:
        pass

def deactivate_keys(keys, focus='turtle'):
    if focus == 'turtle':
        for k in keys:
            turtle.onkey(None, k)
    else:
        for k in keys:
            ws.onkeypress(None, k)

def deactivate_all_keys():
    deactivate_keys(total_t_keys, 'turtle')
    deactivate_keys(game_keys, 'screen')



# initial interface 
def display_main_menu():        
    
    font_size = 18
    upper_left_pos = -200
    deactivate_all_keys()
    tp.clear()
    tp.goto((0, 200))
    tp.write('The Final Project', move=False, align='center', font=("Cambria", font_size + 8, "bold"))
    tp.goto((0, 150))
    tp.write('Weijie XI & Leili', move=False, align='center', font=("Cambria", font_size, "bold"))
    tp.goto((0, 0))
    tp.write('Press (s) to start.', move=False, align='center', font=("Cambria", font_size, "normal"))
    tp.goto((0, -50))
    tp.write('Press (t) to view tutorial.', move=False, align='center', font=("Cambria", font_size, "normal"))
    tp.goto((0, -100))
    tp.write('Press (q) to quit.', move=False, align='center', font=("Cambria", font_size, "normal"))
       
    tp.hideturtle()
    
    turtle.onkey(play_game, 's')
    turtle.onkey(view_tutorial, 't')   
    turtle.onkey(quit_game, 'q')
    turtle.listen()
    ws.mainloop()

