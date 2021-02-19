"""File handling Appending and Writing """

open_file = open('my_file.txt', 'w')

print('This line will write to the file')
open_file.write('This is new file')


open_file.close()
