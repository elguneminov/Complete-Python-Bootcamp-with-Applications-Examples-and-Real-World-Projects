def split_string(name):
    def wrapper():
        split = name().split()
        return split

    return wrapper


@split_string
def normal_string():
    return 'hello world'


print(normal_string())
