x = 0


def welcome():
    global x
    x += 1
    if x < 995:
        print('Welcome to the SS Code Academy')
        welcome()
    else:
        print('It is done Bro!')


welcome()
