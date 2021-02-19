class MyNumber:
    def __iter__(self):
        self.my_number = 1
        return self

    def __next__(self):
        self.my_number += 1
        return self.my_number


obj1 = MyNumber()
my_iterator = iter(obj1)
print(next(my_iterator))
