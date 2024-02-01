import math
import cleanupMethod


def vertical_Displacement_With_Time(x, y):

    z=(x)*(y)+((0.5)*(-9.81)*(y**2))


    return f"Vertical Displcement: {cleanupMethod.cleanup(z)}"

def initial_Vertical_With_Time(x,y):

    z=(((0.5)*(-9.81)*(x**2)-y)/(-x))

    return f"Initial Vertical Velocity: {cleanupMethod.cleanup(z)}"

def time_With_Vertical_Displacement(x,y):

    try:
        z= ((y+math.sqrt((y**2)-(19.62)*(x)))/(9.81))
    except:
        print("Those numbers do not work in the real world")
        z="error"

    return f"Time: {cleanupMethod.cleanup(z)}"

def initial_Velocity_With_Time(x,y):

    z = x-(-9.81)*(y)

    return f"Initial Vertical Velocity: {cleanupMethod.cleanup(z)}"

def final_Velocity_With_Time(x,y):

    z = (x)+(-9.81)*(y)

    return f"Final Vertical Velocity: {cleanupMethod.cleanup(z)}"

def time_With_Final_Velocity(x,y):

    z = (x-y)/(-9.81)

    return f"Time: {cleanupMethod.cleanup(z)}"

def vertical_Displacement_With_Initial_Velocity(x,y):

    z = (((x**2)-(y**2))/((2)*(-9.81)))

    return f"Vertical Displacement: {cleanupMethod.cleanup(z)}"

def initial_Velocity_With_Final_Velocity(x,y):

    z = (x)-math.sqrt((2)*(-9.81)*(y))

    return f"Initial Vertical Velocity {cleanupMethod.cleanup(z)}"

def final_Velocity_With_Initial_Velocity(x,y):

    z = (x)+math.sqrt((2)*(-9.81)*(y))

    return f"Final Vertical Velocity: {cleanupMethod.cleanup(z)}"

#
def horizontal_Displacement_With_Time(x,y):

    z = (x)*(y)

    return f"Horizontal Displacement: {cleanupMethod.cleanup(z)}"

def horizontal_Velocity_With_Time(x,y):

    z = (y)/(x)

    return f"Horizontal Velocity: {cleanupMethod.cleanup(z)}"

def time_With_Horizontal_Displacement(x,y):

    z = (x)/(y)
    return f"Time: {cleanupMethod.cleanup(z)}"


