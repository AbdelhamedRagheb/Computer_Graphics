from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import math


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POLYGON)
    glColor3f(0, 1, 0)
    glVertex2d(0, 0)

    glColor3f(1, 0, 0)
    glVertex2d(1, 0)

    glColor3f(0, 0, 1)
    glVertex2d(0, 1)
    glEnd()

    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Gradient triangle")
glutDisplayFunc(draw)
glutMainLoop()
