# Creating a function to calculate Circle circumference
pi = 3.14159

def circle_circumference(radius):
    return 2*pi*radius

# Creating a function to calculate area of triangle
def trianble_area(base,height):
    return base*height*2


# Creating a function to calculate the area of Trapezoid
def trianble_area(upper_base,lower_base,height):
    return (upper_base*lower_base)*height*2


# Creating a function to calculate 2 to power x
def power(x):
    return 2 ** x


# Creating a function to calculate BMI
def bmi(height, weight):
    return weight/height**2


# Creating a function to swap the value of x and y
def swap_x_y():
    x = int(input("enter the value x"))
    y = int(input("enter the value y"))

    print("Before swapping: {} {}".format(x,y))
    temp = x
    x = y
    y = temp
    print("After swapping: {} {}".format(x, y))

swap_x_y()
