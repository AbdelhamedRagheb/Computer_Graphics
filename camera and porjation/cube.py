from time import sleep
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

from OpenGL.raw.GLU import *

x0 = -1.0  # Line start .
y0 = -1.0
z0 = 1.0
rangle = 0.0


def init_my_scene(Width, Height):
    """  initial parameters. This is called right after the OpenGL window is created.
    """
    ###############################################################################
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear background to black .
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset projection matrix.
    ###########################
    ####  use one of them #####
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    ###########################
    # glOrtho(-2, 2, -2, 2, -5, 5)
    ###############################################################################
    glMatrixMode(GL_MODELVIEW)


def draw_cube(x0, y0, z0, edge_length):
    """ Specification of the line and point positions and their color.
    a cube consists of 8 points
    THIS CUBE HAS TO BE CENTERED AT THE ORIGIN! TODO: WHY?
    x0              , y0              , z0                ###### 1
    x0              , y0 + edge_length, z0                ###### 2
    x0 + edge_length, y0 + edge_length, z0                ###### 3
    x0 + edge_length, y0              , z0                ###### 4

    x0              , y0              , z0 + edge_length  ###### 5
    x0              , y0 + edge_length, z0 + edge_length  ###### 6
    x0 + edge_length, y0 + edge_length, z0 + edge_length  ###### 7
    x0 + edge_length, y0              , z0 + edge_length  ###### 8

    TODO: for each side how many values are common in each transition?
    """
    ######################################################################
    ### top side has 1,2,3,4 points
    ##############
    glColor3f(1.0, 0.0, 0.0)  # red
    glLineWidth(8.0)
    glBegin(GL_LINE_LOOP)
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0 + edge_length, z0)  # 2
    glVertex3f(x0 + edge_length, y0 + edge_length, z0)  # 3
    glVertex3f(x0 + edge_length, y0, z0)  # 4
    glEnd()
    ######################################################################
    ### bottom side has 5,6,7,8 points
    ##############
    glLineWidth(2.0)
    glColor3f(0.0, 0.0, 1.0)  # ~ blue
    glBegin(GL_LINE_LOOP)
    glVertex3f(x0, y0, z0 + edge_length)  # 5
    glVertex3f(x0, y0 + edge_length, z0 + edge_length)  # 6
    glVertex3f(x0 + edge_length, y0 + edge_length, z0 + edge_length)  # 7
    glVertex3f(x0 + edge_length, y0, z0 + edge_length)  # 8
    glEnd()
    # ######################################################################
    ### connect bottom and top sides
    ### 1,2,3,4 => 5,6,7,8
    ### (1, 5) & (2, 6) & (3, 7) & (4, 8)
    ##############
    ##################### connect 1 and 5
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0, z0 + edge_length)  # 5
    glEnd()
    # ##################### connect 2 and 6
    glColor3f(1.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(x0, y0 + edge_length, z0)  # 2
    glVertex3f(x0, y0 + edge_length, z0 + edge_length)  # 6
    glEnd()
    # ##################### connect 3 and 7
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex3f(x0 + edge_length, y0 + edge_length, z0)  # 3
    glVertex3f(x0 + edge_length, y0 + edge_length, z0 + edge_length)  # 7
    glEnd()
    # ##################### connect 4 and 8
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(x0 + edge_length, y0, z0)  # 4
    glVertex3f(x0 + edge_length, y0, z0 + edge_length)  # 8
    glEnd()
    # ######################################################################
    # draw the corners of the the top side
    ##############
    glPointSize(20.0)
    glColor3f(72 / 255.0, 0, 1.0)
    glBegin(GL_POINTS)  # Every vertex specified is a point.
    glVertex3f(x0, y0, z0)  # 1
    glVertex3f(x0, y0 + edge_length, z0)  # 2
    glVertex3f(x0 + edge_length, y0 + edge_length, z0)  # 3
    glVertex3f(x0 + edge_length, y0, z0)  # 4
    glEnd()
    # ######################################################################
    # draw the corners of the the bottom side
    glPointSize(12.0)
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POINTS)
    glVertex3f(x0, y0, z0 + edge_length)  # 5
    glVertex3f(x0, y0 + edge_length, z0 + edge_length)  # 6
    glVertex3f(x0 + edge_length, y0 + edge_length, z0 + edge_length)  # 7
    glVertex3f(x0 + edge_length, y0, z0 + edge_length)  # 8
    glEnd()
    # ######################################################################
    # # TODO: for fun :D
    # glTranslatef(x0, y0, z0)  # Shift to convenient position.
    # glutWireTeapot(.1)


def DrawGLscene():
    global rangle

    glClear(GL_COLOR_BUFFER_BIT)  # Clear screen and depth buffer.
    ###################################################################################
    # # TODO: draw some points, comment the code for cubes if you want to see this
    # glPointSize(12.0)
    # glLoadIdentity()
    # glColor3f(0, 0, 1)
    # glBegin(GL_POINTS)
    # # try one of those vertices
    # # glVertex3f(0, 0, -5)  # TODO: try this and you will see the point, why?
    # # glVertex3f(0, 0, 0)  # TODO: try this, you will see nothing, why?
    # # glVertex3f(0, 0, -100)  # TODO: try this and you will see the point, why?
    # glVertex3f(0, 0, -101)  # TODO: try this, you will see nothing, why?
    # glEnd()
    size = [1.0, 1.0, 1.0]  # Change size if desired.
    location = [0.0, 0.0, -5.0]



    # ########################################
    # first cube, rotate around x
    # ########################################
    glLoadIdentity()
    glTranslatef(location[0], location[1], location[2])  # Shift to convenient position.
    glScale(size[0], size[1], size[2])  # Change size if desired.
    glRotatef(rangle, 1.0, 0.0, 0.0)  # Rotate cube around X.
    draw_cube(-1.0, -1.0, -1.0, 2.0)  # Largest cube.
    # ########################################
    # # middle cube, rotate around y
    # ########################################
    glLoadIdentity()
    glTranslatef(location[0], location[1], location[2])  # Shift to convenient position.
    glScale(size[0], size[1], size[2])  # Change size if desired.
    glRotatef(rangle, 0.0, 1.0, 0.0)  # Rotate cube around y.
    draw_cube(-0.9, -0.9, -0.9, 1.8)  # Intermediate size cube.
    # ######################################
    # # last cube, rotate around y
    # ########################################
    glLoadIdentity()
    glTranslatef(location[0], location[1], location[2])  # Shift to convenient position.
    glScale(size[0], size[1], size[2])  # Change size if desired.
    glRotatef(rangle, 0.0, 0.0, 1.0)  # Rotate cube around z.
    draw_cube(-0.8, -0.8, -0.8, 1.7)  # Intermediate size cube.
    ######
    rangle += 0.1
    glutSwapBuffers()


if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"Perspective: 45.0, float(Width)/float(Height), 0.1, 100.0")
    glutDisplayFunc(DrawGLscene)
    glutIdleFunc(DrawGLscene)
    init_my_scene(1000, 1000)
    glutMainLoop()
