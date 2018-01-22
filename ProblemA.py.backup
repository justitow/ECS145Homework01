class polynom:
    def __init__(self, poly_list):
        self.poly = list(poly_list)  # calling list makes sure to make a new instance
        self.poly = self.trim_zeroes(self.poly)

    # adds two things, I used this in the map function later on, there is probably
    # something built in to python, but I couldn't find it
    def element_add(self, x, y):
        return x + y
    def element_sub(self, x, y):
        return x - y

    # %%%%%%% to test pycharm
    # removes any zeros that are prepended to the list
    # if the list is all zeroes, it turns it into an empty list
    # returns nothing
    def trim_zeroes(self, trim_poly):
        zero_index = 0
        while zero_index < len(trim_poly) and trim_poly[zero_index] == 0:
            zero_index += 1
        if zero_index >= len(trim_poly):
            return []
        else:
            return trim_poly[zero_index:]

    # returns a list that is the addition of two polynomials
    def __add__(self, other):
        # need to check if other's type is polynom?
        diff = len(self.poly) - len(other.poly)
        if diff > 0:
            return  self.trim_zeroes(map(self.element_add, self.poly, [0]*diff + other.poly))
        else:
            return self.trim_zeroes(map(self.element_add, [0]*(-diff) + self.poly, other.poly))

    def __sub__(self, other):
        diff = len(self.poly) - len(other.poly)
        if diff > 0:
            return  self.trim_zeroes(map(self.element_sub, self.poly, [0]*diff + other.poly))
        else:
            return self.trim_zeroes(map(self.element_sub, [0]*(-diff) + self.poly, other.poly))

    """
    def __mul__(self, other):

    def intg(self, a, b):

    def drv(self, a, b):
    """
