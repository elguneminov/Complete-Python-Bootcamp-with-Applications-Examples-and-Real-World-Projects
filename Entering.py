""" Python Exception Handling Using try, except and finally statement"""


def entering(age):
    if age < 18:
        raise ValueError
    else:
        print('You can enter to the club')


try:
    entering(10)
except:
    print('Your age is less than 18,and you can not enter')
