import math


def vertical_Displacement_With_Time(x, y):

    z=(x)*(y)+((0.5)*(-9.81)*(y**2))


    return f"Vertical Displcement: {z}"

def initial_Vertical_With_Time(x,y):

    z=(((0.5)*(-9.81)*(x**2)-y)/(-x))

    return f"Initial Vertical Velocity: {z}"

def time_With_Vertical_Displacement(x,y):

    try:
        z= ((y+math.sqrt((y**2)-(19.62)*(x)))/(9.81))
    except:
        print("Those numbers do not work in the real world")
        z="error"

    return f"Time: {z}"

def initial_Velocity_With_Time(x,y):

    z = x-(-9.81)*(y)

    return f"Initial Vertical Velocity: {z}"

def final_Velocity_With_Time(x,y):

    z = (x)+(-9.81)*(y)

    return f"Final Vertical Velocity: {z}"

def time_With_Final_Velocity(x,y):

    z = (x-y)/(-9.81)

    return f"Time: {z}"

def vertical_Displacement_With_Initial_Velocity(x,y):

    z = (((x**2)-(y**2))/((2)*(-9.81)))

    return f"Vertical Displacement: {z}"

def initial_Velocity_With_Final_Velocity(x,y):

    z = (x)-math.sqrt((2)*(-9.81)*(y))

    return f"Initial Vertical Velocity {z}"

def final_Velocity_With_Initial_Velocity(x,y):

    z = (x)+math.sqrt((2)*(-9.81)*(y))

    return f"Final Vertical Velocity: {z}"

#
def horizontal_Displacement_With_Time(x,y):

    z = (x)*(y)

    return f"Horizontal Displacement: {z}"

def horizontal_Velocity_With_Time(x,y):

    z = (y)/(x)

    return f"Horizontal Velocity: {z}"

def time_With_Horizontal_Displacement(x,y):

    z = (x)/(y)
    return f"Function is called with inputs: {x}, {y}"


