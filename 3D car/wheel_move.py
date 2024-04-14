from time import sleep

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import static_car

theta = 0  ###### Q2
forward = False  ###### Q2


def draw():
    global theta  ###### Q2
    global forward  ###### Q2

    # clear
    glClearColor(0, 0, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    # # #########################################
    # AXES
    glLoadIdentity()
    static_car.reposition_camera()
    static_car.draw_axes()

    #########################################
    ######## bottom cube
    glColor3f(1, 0, 0)  # red
    glLoadIdentity()
    static_car.reposition_camera()
    glTranslate(0, 0, 0)
    glScale(4, 1, 2)
    glutWireCube(1)
    #########################################
    ########## top cube
    glColor3f(1, 0, 0)  # still red
    glLoadIdentity()
    static_car.reposition_camera()
    glTranslate(0, 1 - .15, 0)
    glScale(2, .7, 1.5)
    glutWireCube(1)
    #########################################
    ############# wheels
    glColor3f(0, 0, 1)
    draw_rotated_wheel(loc_x=+2, loc_y=-0.5, loc_z=-1, theta=theta)  # right front wheels
    draw_rotated_wheel(loc_x=-2, loc_y=-0.5, loc_z=-1, theta=theta)  # right rear wheels
    draw_rotated_wheel(loc_x=+2, loc_y=-0.5, loc_z=1, theta=theta)  # left front wheels
    draw_rotated_wheel(loc_x=-2, loc_y=-0.5, loc_z=1, theta=theta)  # left rear wheels
    #########################################
    ############# headlight bulbs
    glColor3f(1, 1, 0)
    static_car.draw_headlight_bulb(loc_x=+2, loc_y=0, loc_z=-.5)  # right bulb
    static_car.draw_headlight_bulb(loc_x=+2, loc_y=0, loc_z=+.5)  # left bulb
    #########################################
    glutSwapBuffers()  ###### from Q2

    theta = theta + (0.5 if forward else -.5)  # from Q2: increase theta


def draw_rotated_wheel(loc_x, loc_y, loc_z, theta):  ###### from Q2 : added the rotation angle for the wheels
    glLoadIdentity()
    static_car.reposition_camera()
    glTranslate(loc_x, loc_y, loc_z)
    glRotate(theta, 0, 0, -1)
    glutWireTorus(0.15, 0.35, 10, 12)


if __name__ == "__main__":  # TODO try to remove this?
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  ###### from Q2: used GLUT_DOUBLE buffer
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Moving Car")
    glutPositionWindow(100, 200)
    static_car.init_projection()
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()

###############################
# RECIPE FOR ANIMATION
# 1) replace GLUT_SINGLE >> GLUT_DOUBLE
# 2) replace glFlush >> glutSwapBuffers
# 3) use glutIdleFunc(draw_function)
# 4) do some transformations !
###############################
