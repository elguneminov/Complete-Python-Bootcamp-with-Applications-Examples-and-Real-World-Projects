""" Python Exception Handling Using try, except and finally statement"""


def exam(first_exam, second_exam):
    if first_exam < 50 or second_exam < 50:
        raise Exception
    elif second_exam < 50 or first_exam > 50:
        raise Exception
    elif second_exam > 50 or first_exam < 50:
        raise Exception
    else:
        print('You got this')


first_result = int(input('Enter first exam result:'))
second_result = int(input('Enter second result:'))

try:
    exam(first_result, second_result)
except  :
    print('One of your exam result is less than 50')
else:
    print('Your all exam results are grater than 50')
