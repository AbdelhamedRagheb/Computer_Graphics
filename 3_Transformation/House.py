from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw1():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1.0, 0, 1.0)
    #####################
    # triangle
    glBegin(GL_POLYGON)
    glVertex2d(0.2, 0.2)
    glVertex2d(-0.2, 0.2)
    glVertex2d(0, 0.5)
    glEnd()
    ######################
    # rectangle
    glColor3f(0.0, 1, 0)
    glBegin(GL_POLYGON)
    glVertex2d(0.2, 0.2)
    glVertex2d(-0.2, 0.2)
    glVertex2d(-0.2, -0.2)
    glVertex2d(0.2,-0.2)
    glEnd()
    # vertical axis
    glColor3f(0.0, 0, 1)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(0, 1)
    glEnd()
    #####################
    # horizontal axis
    glColor3f(1.0, 0, 0)
    glBegin(GL_LINES)
    glVertex2d(0, 0)
    glVertex2d(1, 0)
    glEnd()
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(500, 500)  # Set the window's initial width & height
    glutInitWindowPosition(0, 0)  # Set the window's initial width & height
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Home sweet home")
    glutDisplayFunc(draw1)
    glutMainLoop()
