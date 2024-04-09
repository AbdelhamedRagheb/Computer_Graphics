from OpenGL.GLUT import *
from OpenGL.GL import *


def draw_tringle(v1, v2, v3):
    glBegin(GL_LINE_LOOP)
    glVertex2d(v1[0], v1[1])
    glVertex2d(v2[0], v2[1])
    glVertex2d(v3[0], v3[1])
    glEnd()


def draw():
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

    # yellow tringle
    glColor3d(1, 1, 0)
    draw_tringle((-0.5, -0.5), (0.5, -0.5), (0.5, 0.5))

    # grean tringle
    glColor3d(0, 1, 0)
    draw_tringle((-0.5, 0), (0.5, 0), (0.5, -0.5))
    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Tringle")  # the b -> refere to byte
    glutDisplayFunc(draw)
    glutMainLoop()
