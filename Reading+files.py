"""File handling Reading and Writing """

open_file = open('Test.txt', 'r')

for element in open_file.readlines():
    print(element)

open_file.close()
