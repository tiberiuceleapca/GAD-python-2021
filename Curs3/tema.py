import modul_tema as mt

# ex 1
def sum_of_params(*args):
    s = 0
    for i in args:
        try:
            s += i
        except TypeError as e:
            pass

    return s


# ex 2
def check_if_integer():
    value = input('Enter integer: ')

    try:
        value_int = int(value)

    except ValueError as e:
        return 0

    return value_int


if __name__ == "__main__":
    # ex 1
    print('Sum of params:', sum_of_params(1, 5, -3, "abc", [12, 56, "cad"]))

    # ex 2
    print('Integer:', check_if_integer())

    # ex 3
    n = 10
    print(f'Sum from 0 to {n}:', mt.sum_zero_to_n(n))
    print(f'Sum of even numbers from 0 to {n}:', mt.sum_even_zero_to_n(n))
    print(f'Sum of odd numbers from 0 to {n}:', mt.sum_odd_zero_to_n(n))
