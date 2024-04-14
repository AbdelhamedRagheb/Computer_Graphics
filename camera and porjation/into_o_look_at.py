from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glColor3d(0.0, 0.8, 1.0)

    # default look at
    # gluLookAt(
    #     0, 0, 0,
    #     0, 0, -1,
    #     0, 1, 0
    # )

    # move the camera nearer to the point
    gluLookAt(
        0, 0, -1, # porgation in defult cut cube of 1 in all
        0, 0, -2,
        0, 1, 0
    )

    glPointSize(12.0)
    glBegin(GL_POINTS)
    glVertex3f(0, 0,-1)
    glEnd()
    glFlush()


# boilerplate
glutInit()
glutInitWindowSize(500, 500)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"look at intro")
glutDisplayFunc(draw)
glutMainLoop()