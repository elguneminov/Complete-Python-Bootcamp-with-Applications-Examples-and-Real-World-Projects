""" Generators  yield """
""" Memory storing problem """


def square_number(numbers): # Your python will return generator object
    for x in numbers:
        yield x*x


my_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 345, 5764, 234, 1, 6, 3, 7, 23, 987, 456, 34, 8, 456, 678]
new_list = square_number(my_list)
print(next(new_list))
