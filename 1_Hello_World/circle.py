from OpenGL.GL import *
from OpenGL.GLUT import *
from math import *


# import numpy as np


def draw_axis():
    # x axis
    glColor3d(1, 0, 0)
    glBegin(GL_LINE_STRIP)
    glVertex2d(-1, 0)
    glVertex2d(1, 0)
    glEnd()
    # y axis
    glColor3d(0, 0, 1)
    glBegin(GL_LINE_STRIP)
    glVertex2d(0, -1)
    glVertex2d(0, 1)
    glEnd()


def draw_circle(resolution=1, r=0.5):
    # draw circle
    glBegin(GL_LINE_LOOP)
    for q in range(0, 361, resolution):  # if you want to use float resolution try np.range
        x = r * cos(q * pi / 180)
        y = r * sin(q * pi / 180)
        glVertex2d(x, y)
    glEnd()


def draw():
    draw_axis()
    # yellow circle
    glColor3d(1, 1, 0)
    # glColor3bv() # -> (255,255,255)
    draw_circle(1)

    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Circle")
    glutDisplayFunc(draw)
    # print("Hello world")
    glutMainLoop()
