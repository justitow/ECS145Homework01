class polynom:
    def __init__(self, poly_list):
        self.poly = list(poly_list)
        self.trim_zeros()

    #adds two things, I used this in the map function later on, there is probably
    #something built in to python, but I couldn't find it
    def element_add(self, x, y):
        return x + y
    def element_sub(self, x, y):
        return x - y

    def trim_zeros(self):
        zero_index = 0
        while zero_index < len(self.poly) and self.poly[zero_index] == 0:
            zero_index += 1
        if zero_index >= len(self.poly):
            self.poly = []
        else:
            self.poly = self.poly[zero_index:]

    def __add__(self, other):
        # need to check if other's type is polynom?
        diff = len(self.poly) - len(other.poly)
        if diff > 0:
            return  map(self.element_add, self.poly, [0]*diff + other.poly)
        else:
            return map(self.element_add, [0]*(-diff) + self.poly, other.poly)


    def __sub__(self, other):
        diff = len(self.poly) - len(other.poly)
        if diff > 0:
            return  map(self.element_sub, self.poly, [0]*diff + other.poly)
        else:
            return map(self.element_sub, [0]*(-diff) + self.poly, other.poly)

    """
    def __mul__(self, other):

    def intg(self, a, b):

    def drv(self, a, b):
    """
