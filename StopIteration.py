""" StopIteration object"""

list1 = [1, 2, 3, 5, 7, 8, 9, 70, 454, 354, 234, 123, 1567, 89]
new_list = iter(list1)
for x in list1:
    print(x)

while True:
    try:
        print(next(new_list))
    except StopIteration:
        break
