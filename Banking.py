while True:
    operation = input('Welcome to the SS Banking\n'
                      'These are our operations:\n'
                      '1:Take money\n'
                      '2:Put money\n'
                      '3:Money transfer\n'
                      'Q:Quitting\n')
    if operation == '1':
        balance = int(input('How much money do you have? :'))
        money = int(input('How much money do you want to take?: '))
        if balance < money:
            print('You can not do this!\nYour balance in not enough to this operation!')
            break
        else:
            print("Your money: ", (balance - money), '$')
    elif operation == '2':
        money = int(input('How much money do you want to put?: '))
        balance = int(input('How much money do you have?'))
        print('Your new balance is: ', (money + balance), '$')
    elif operation == '3':
        balance = int(input('How much money do you have?'))
        transfer = int(input('How much money will you transfer?: '))
        if balance > transfer:
            print('You transferred :', transfer, '$')
            print('Your balance is: ', (balance - transfer), '$')
        elif balance < transfer:
            print('There is no enough money to do this operation')
            break
    elif operation == 'Q':
        print('Quitting from application!')
        break
    else:
        print('Invalid operation!')
        break
