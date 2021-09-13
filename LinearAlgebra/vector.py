import math


class Vector(object):
    def __init__(self, coordinates):  # initiate values of vectors and dimensions
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):  # to print coordianates
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):  # to check if vectors are equal
        return self.coordinates == v.coordinates

    def magnitude(self):  # to find magnitude of vector
        sq_sum = [x**2 for x in self.coordinates]
        return math.sqrt(sum(sq_sum))

    def normal(self):  # to find normal vector of given vector
        try:
            magnitude = self.magnitude()
            return self.scalar(1/magnitude)

        except ZeroDivisionError:
            raise Exception("Cant find Normal of Zero vector")

    def plus(self, v):  # add 2 vectors
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v[i])
        return Vector(new_coordinates)

    def minus(self, v):  # subtract 2 vectors
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] - v[i])
        return Vector(new_coordinates)

    def scalar(self, c):  # scalar multiplication of vector and number
        new_coordinates = []
        new_coordinates = [round(c*x, 3) for x in self.coordinates]
        return Vector(new_coordinates)
