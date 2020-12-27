def calculate():

    operation = input('''
Please type the math operation you would like to compete:
+ for addition
- for subtaction
* for multiplication
/ for division
''')
    number_1 = float(input("please enter the first number: "))
    number_2 = float(input("please enter the second number: "))
    if operation == '+':
       print('{} + {} = '.format(number_1 , number_2))
       print(number_1 + number_2)

    elif operation == '-':
         print('{} - {} = '.format(number_1, number_2))
         print(number_1 - number_2)

    elif operation == '*':
         print('{} * {} = '.format(number_1, number_2))
         print(number_1 * number_2)

    elif operation == '/':
         print('{} / {} = '.format(number_1, number_2))
         print(number_1 / number_2)

    else:
         print('You enter a wrong operator!')
    again()

def again():
    calculation_again = input(''' Do you want to calculate again?
    please type Y for Yes and N for No
    ''')
    if calculation_again.upper() == 'Y':
        calculate()
    elif calculation_again.upper() == 'N':
        print('Bye Bye ,thank you for coming.')
    else:
        again()

calculate()
