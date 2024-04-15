from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

####################################
############## design ##############
####################################
# 1. a ball with state (x, y)
# 2. game bat with state (x, y)
# 3. collision detection
#       - ball vs bat => make it bounce
#       - ball vs wall => to remain within boundaries
# 4. tracking scores in globals
# 5. handling inputs
# 6. timer
####################################
########### constants ##############
####################################
FONT_DOWNSCALE = 0.13
FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

INTERVAL = 10  # try  1000 msec


####################################
# RECT CLASS
class Rectangle:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top


####################################
########### game state #############
####################################
current_delta_X = 1
current_delta_y = 1

current_ball = Rectangle(140, 140, 160, 160)  # initial rect of the ball # TODO: try different numbers
current_wall = Rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
current_player = Rectangle(0, 0, 60, 10)  # initial rect of the bat # TODO: try different numbers

current_pc_result = 0
current_player_result = 0

current_mouse_x = 0


####################################
######## graphics helpers ##########
####################################
# Initialization
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)  # ortho or perspective NO BRAINER
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)  # l,r,b,t,n,f

    glMatrixMode(GL_MODELVIEW)


def draw_rectangle(rect):
    glPushMatrix()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()
    glPopMatrix()


def draw_text(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glPushMatrix()  # remove the previous transformations
    # glScale(0.13,0.13,1)  # TODO: Try this line
    glTranslate(x, y, 0)
    glScale(FONT_DOWNSCALE, FONT_DOWNSCALE,
            1)  # when writing text and see nothing downscale it to a very small value .001 and draw at center
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    glPopMatrix()


####################################
######## Collision Detection #######
####################################
def check_ball_wall(_ball, _wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    if _ball.right >= _wall.right:
        return FROM_RIGHT
    if _ball.left <= _wall.left:
        return FROM_LEFT
    if _ball.top >= _wall.top:
        return FROM_TOP
    if _ball.bottom <= _wall.bottom:
        return FROM_BOTTOM

    # Otherwise, this function returns None


def check_ball_bat(_ball, _player):  # Collision Detection between Ball and Bat
    # _ball and _player can be replaced by the global states
    horizontal_check = _player.left <= _ball.left <= _ball.right <= _player.right  # horizontally lying inside
    vertical_check = _ball.bottom <= _player.top  # vertically overlapping
    return vertical_check and horizontal_check


####################################
############# callbacks  ###########
####################################

def keyboard_callback(key, x, y):
    if key == b"q":
        sys.exit(0)


def mouse_callback(x, y):
    global current_mouse_x
    current_mouse_x = x  # we only track the x coordinate


####################################
############# timers  ##############
####################################

def game_timer(v):
    display_lecture()
    print(v)
    glutTimerFunc(INTERVAL, game_timer, v + 1)  # TODO: replace 1 by v+1


########################################################


def display_lecture():
    global current_delta_X
    global current_delta_y

    global current_pc_result
    global current_player_result

    glClear(GL_COLOR_BUFFER_BIT)
    # draw_rectangle(RECT(WINDOW_WIDTH, WINDOW_HEIGHT, 30, 30)) # TODO draw any rect

    string = "PC : " + str(current_pc_result)
    draw_text(string, 10, 440)
    string = "Player :  " + str(current_player_result)
    draw_text(string, 10, 400)

    current_ball.left = current_ball.left + current_delta_X  # updating ball's coordinates
    current_ball.right = current_ball.right + current_delta_X
    current_ball.top = current_ball.top + current_delta_y
    current_ball.bottom = current_ball.bottom + current_delta_y

    glColor(1, 1, 1)  # White color

    draw_rectangle(current_ball)

    # print(Test_Ball_Wall(ball,wall))

    if check_ball_wall(current_ball, current_wall) == FROM_RIGHT:
        current_delta_X = -1

    if check_ball_wall(current_ball, current_wall) == FROM_LEFT:
        current_delta_X = 1

    if check_ball_wall(current_ball, current_wall) == FROM_TOP:
        current_delta_y = -1

    if check_ball_wall(current_ball, current_wall) == FROM_BOTTOM:
        current_delta_y = 1
        current_pc_result = current_pc_result + 1  # pc gets a point

    current_player.left = current_mouse_x - 30
    current_player.right = current_mouse_x + 30
    draw_rectangle(current_player)

    if check_ball_bat(current_ball, current_player):  # returns true if the ball hits the bat without falling
        # same as FROM_BOTTOM
        current_delta_y = 1
        current_player_result = current_player_result + 1  # player gets a point

    glutSwapBuffers()


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Simple Ball Bat OpenGL game")
    glutDisplayFunc(display_lecture)
    glutTimerFunc(INTERVAL, game_timer, 1)  # timer function
    glutKeyboardFunc(keyboard_callback)  # keyboard listen
    glutPassiveMotionFunc(mouse_callback)  # mouse listen
    init()
    glutMainLoop()
