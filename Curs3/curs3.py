import my_module
import random
from my_package import my_module_from_package as m


# 1
def random_choice():
    choices = [x for x in range(11)]

    while 1:
        rd = random.choice(choices)

        if rd % 3 == 0:
            break
        print(f'Random choice is {rd}')

    print(f'Exited with {rd}')


# 2
def suma(a, b):
    return a + b


# 3
def modify_list(lst):
    lst.append(4)


# 4
def copiaza(lst):
    l = lst.copy()
    l.append(4)


# 5
def param_args(a, b, *args):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'args = {args}')


# 6
def param_kwargs(a, b, **kwargs):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'kwargs = {kwargs}')


# 7
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# 8
def playing_with_exceptions():
    var = input('enter an integer: ')
    try:
        var_int = int(var)
        print(something)
    except ValueError as e:
        print("You have to enter an integer!", e)
    except NameError as e:
        print("Your variable is undefined.", e)
    else:
        print("There are no exceptions.")
    finally:
        print("I don't care what happens above me.")


# 9
def playing_with_globals():
    global msg
    msg = "Hello, there!"


# 10
def test_name():
    print(f'I\'m a function from {__name__}')


if __name__ == '__main__':
    # 1
    random_choice()

    # 2
    print(suma(5, 7))

    # 3
    l = [1, 2, 3]
    modify_list(l)

    print(l)  # afiseaza [1, 2, 3, 4]

    # 4 - l = [1, 2, 3, 4]
    copiaza(l)
    print(l)  # l ramane tot [1, 2, 3, 4]

    # 5
    param_args(1, 2, 3, 4, "abc")

    # 6
    param_kwargs(1, 2, x=2, y=3, name="john")

    # 7
    n = 9
    print(f'fibo({n}) = {fibonacci(n)}')

    # 8
    playing_with_exceptions()

    # 9
    playing_with_globals()
    print(msg)

    # 10
    test_name()

    # 11
    print(my_module.my_var)
    my_module.show_my_var()

    # 12
    print(m.my_package_var)
    m.show_my_package_var()
