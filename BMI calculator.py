BMI Calculator code
# BMI = Weight / Height^2    kg and m

def convert_to_m(height):
    return height/100


def calculate_bmi(height, weight):
    return weight/height**2


def bmi_test(bmi):
    print('Your bmi is {}'.format(round(bmi, 2)))
    if bmi < 18.5:
        print('You\'d better eat more!')
    elif bmi >= 18.5 and bmi < 24:
        print('Good job!')
    else:
        print('You\'d better to some exercises')


def bmi_app():
    height = int(input('What\'s your height (in cm)? '))
    height = convert_to_m(height)
    weight = int(input('what\'s your weight (in kg) '))
    bmi = calculate_bmi(height, weight)
    bmi_test(bmi)


bmi_app()

# how to improve?
# Q1 what if the weight is not integer? e.g. 62.5
