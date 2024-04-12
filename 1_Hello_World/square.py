from OpenGL.GLUT import *
from OpenGL.GL import *
from circle import draw_axis


def draw():
    glMatrixMode(GL_MODELVIEW)  # To operate on Model-View matrix
    glLoadIdentity()
    draw_axis()
    glColor3d(0.0, 0.8, 1.0)
    # rotate then scale
    #################################
    # print("glLoadIdentity\n", glGetFloatv(GL_MODELVIEW_MATRIX)) # -> make error ??
    # glScale(1.5, 1, 1)  # scale on x by 1.5
    # print("glScale\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    # glRotate(60, 0, 0, 1)  # rotate around z by 60 # counterclockwise
    # print("glRotate\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    #################################
    # Scale then rotate
    #################################
    # print("glLoadIdentity\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    glRotate(60, 0, 0, 1)  # rotate around z by 60 # counterclockwise
    #print("glScale\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    glScale(1.5, 1, 1)  # scale on x by 1.5
    # print("glRotate\n", glGetFloatv(GL_MODELVIEW_MATRIX))
    #################################
    glBegin(GL_POLYGON)
    glVertex2d(-0.5, -0.5)
    glVertex2d(0.5, -0.5)
    glVertex2d(0.5, 0.5)
    glVertex2d(-0.5, 0.5)
    glEnd()

    glFlush()


if __name__ == "__main__":
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow(b"Square")
    glutDisplayFunc(draw)
    glutMainLoop()
