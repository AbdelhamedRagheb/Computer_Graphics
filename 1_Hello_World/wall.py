from OpenGL.GL import *
from OpenGL.GLUT import *
from circle import draw_axis


def draw_rectangular(v1, v2, v3, v4):
    glBegin(GL_POLYGON)
    glVertex2d(v1[0], v1[1])
    glVertex2d(v2[0], v2[1])
    glVertex2d(v3[0], v3[1])
    glVertex2d(v4[0], v4[1])
    glEnd()


def draw():
    draw_axis()  # draw axis in x, y
    glColor3f(1.0, 0.5, 1.0)
    ####################################
    # Head
    ####################################
    draw_rectangular((0.2, 0.9), (-0.2, 0.9), (-0.2, 0.6), (0.2, 0.6))
    glColor3f(1, 1, 1)
    ####################################
    # right  eye
    ####################################
    draw_rectangular((0.05, 0.8), (0.15, 0.8), (0.15, 0.7), (0.05, 0.7))
    ####################################
    # left  eye
    ####################################
    draw_rectangular((-0.05, 0.8), (-0.15, 0.8), (-0.15, 0.7), (-0.05, 0.7))
    glColor3f(1.0, 0.5, 1.0)  # return to the main color
    ####################################
    # NICK
    ####################################
    draw_rectangular((0.1, 0.6), (-0.1, 0.6), (-0.1, 0.4), (.1, 0.4))
    # glBegin(GL_POLYGON)
    # glVertex2d(0.1, 0.6)
    # glVertex2d(-0.1, 0.6)
    # glVertex2d(-0.1, 0.4)
    # glVertex2d(0.1, 0.4)
    # glEnd()

    ####################################
    # Stomach
    ####################################
    draw_rectangular((0.5, 0.4), (-0.5, 0.4), (-0.5, -0.2), (0.5, -0.2))

    # glBegin(GL_POLYGON)
    # glVertex2d(0.5, 0.4)
    # glVertex2d(-0.5, 0.4)
    # glVertex2d(-0.5, -0.2)
    # glVertex2d(0.5, -0.2)
    # glEnd()

    ####################################
    #  Left leg
    ####################################
    glBegin(GL_POLYGON)
    glVertex2d(-0.3, -0.2)
    glVertex2d(-0.5, -0.2)
    glVertex2d(-0.5, -0.5)
    glVertex2d(-0.3, -0.5)
    glEnd()

    ####################################
    # right leg
    ####################################
    glBegin(GL_POLYGON)
    glVertex2d(0.5, -0.2)
    glVertex2d(0.3, -0.2)
    glVertex2d(0.3, -0.5)
    glVertex2d(0.5, -0.5)

    ############
    # BAD POLYGON
    # TODO : try this bad polygon -> the same result
    # ->
    ############
    # glVertex2d(0.3, -0.2)
    # glVertex2d(0.5, -0.2)
    # glVertex2d(0.3, -0.5)
    # glVertex2d(0.5, -0.5)
    ############
    glEnd()
    ####################################
    # right arm
    ####################################
    # # 6: right arm
    glBegin(GL_LINES)
    glVertex2d(0.5, 0.3)
    glVertex2d(0.7, -0.2)
    glEnd()

    ####################################
    # left arm
    ####################################
    # 7: left arm
    glBegin(GL_LINES)
    glVertex2d(-0.5, 0.3)
    glVertex2d(-0.7, -0.2)
    glEnd()

    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Wall")
    glutDisplayFunc(draw)
    glutMainLoop()
