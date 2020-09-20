import random

# functions guides


def name_of_function(name):
    """Best Practice to create a function
    * naming snake case
    * pay attention to argument"""
    print("name_of_function")
    print("Hello" + name)


name_of_function("Leo")


def return_value_add_function(num1, num2):
    print("return_value_add_function")
    print(num1+num2)
    return num1 + num2


return_value_add_function(3,5)

def function_arg_print(name):
    print(f'Hello{name}')

function_arg_print("Leo")

def function_arg_print_default_value(name='Carlos Augusto'):
    print(f'Hello{name}')

function_arg_print_default_value()

def add_num(num1, num2):
    return num1+num2

add_num(10,20)

# Boolean handling
def even_check(num):
    result = num % 2 == 0
    print(result)
    return result

even_check(10)

def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass

    return False

check_even_list([40,50,22,25,13,11,5])


def return_even_numbers(num_list):
    # Variables
    even_numbers=[]
    odd_numbers=[]
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    print(odd_numbers)
    print(even_numbers)
    return even_numbers

return_even_numbers([1,2,3,4,5,6,7,8,9,0])


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    print(employee_of_month, current_max)
    return (employee_of_month, current_max)

work_hours = [('Caio',100),('Leo', 400),('John Armless',800)]
employee_check(work_hours)


def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist


def player_guess():
    guess=''

    while guess not in ['0','1','2']:
        guess = input("pick a number: 0,1, or 2")

        return int (guess)


def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("Correct!")
    else:
        print("wrong guess!")
        print(mylist)