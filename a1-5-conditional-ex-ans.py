
# Q1 - create a function to determine whether a number is even or odd by print out a line saying "The entered number is odd"




def odd_or_even(x):
    if x % 2 == 0:
        print("The number {} is even".format(x))
    else:
        print("The number {} is odd".format(x))


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_even(x):
    return x % 2 == 0




# Q2 - create a funciton to compare two integer. output the bigger number
def compare(x ,y):
    if x> y:
        return x
    else:
        return y


# Q3 - create a function to compare three integer. output the bigger number
def compare(x, y, z):
    return compare(x, compare(y, z))


# Q4 - create a function to compare 4 integer. output the bigger number
def compare(a, b, c, d):
    return compare(compare(a, b), compare(c, d))


# Q4 - write a function to check whether a year is a leap year. return True or False
def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


# another answer without if then else
def leap_year(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)


# Q5 - write a function to input 3 anglers of a triangle and check whether that is a valid triangle. return True or False
def is_triangle(a, b, c):
    if a + b + c == 180:
        return True
    else:
        return False

# another shorthand
def is_triangle(a, b, c):
    return a + b + c == 180
