import math


class Coordinate:
    """ Coordonata in spatiul 2D, care contine pozitiile x si y """

    def __init__(self, x, y):
        """ Constructor cu parametri """
        self.x = x
        self.y = y


    def distance(self, c2):
        p1 = (self.x - c2.x)**2
        p2 = (self.y - c2.y)**2
        return math.sqrt(p1 + p2)

    def __str__(self):
        return f"x = {self.x}\ny = {self.y}"


if __name__ == '__main__':
    c = Coordinate(0, 0)
    c1 = Coordinate(3, 3)

    print(c.distance(c1))

    print(c)
