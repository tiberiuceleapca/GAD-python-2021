def compute_least_common_multiple(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm


class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def inverse(self):
        return Fractie(self.numitor, self.numarator)

    def __add__(self, other):
        lcm = compute_least_common_multiple(self.numitor, other.numitor)

        numarator = self.numarator * (lcm / self.numitor) + other.numarator * (lcm / other.numitor)

        return Fractie(numarator, lcm)

    def __sub__(self, other):
        lcm = compute_least_common_multiple(self.numitor, other.numitor)

        numarator = self.numarator * (lcm / self.numitor) - other.numarator * (lcm / other.numitor)

        return Fractie(numarator, lcm)


if __name__ == '__main__':
    f1 = Fractie(2, 6)
    f2 = Fractie(5, 4)

    print("initial: ", f1, "and", f2)
    print("add: ", f1 + f2)
    print("sub: ", f1 - f2)
    print("inverse: ", f1.inverse())
