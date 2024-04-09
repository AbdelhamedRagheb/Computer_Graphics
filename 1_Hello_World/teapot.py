from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_teapot():
    glColor3d(0, 0, 1)  # color of teapot
    glutWireTeapot(0.2)  # draw teabot
    # glColor3d(1,0,0) #color of cube
    # glutWireCube(0.5) # draw cube

    glFlush()
    print("Teapot")


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # single refere to single buffer and rgb is the color mode
    glutCreateWindow(b"Teapot")  # name of window
    glutDisplayFunc(draw_teapot)  # your draw function ex: teabot from lib
    glutMainLoop()  # to repeat all time
