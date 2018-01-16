# This is a Polynomial Class that perfomrs various operations
# Integration over an interval
# Derivative of a Polynomial
# Addition, Subtraction and Multiplication

class polynom:
    'Polynomial Class'
    def __init__(self, list):
        'Constructor for Single Polynomial'

        list = self.removeZero(list)
        self.poly = list # A polynomial represented as a list

    def intg(self, a, b):
        'Integral over [a,b] \
        evaluates as F(B) - F(A)\
        where F(x) = d/dx(f(x))'
        F = []
        F = self.adrv()
        out = 0
        index = len(F) - 1
        #Evaluate F(x) as sum(i * x^index)

        for i in F:
            out += (i * (b ** index)) - (i * (a ** index))
            index -= 1

        out = self.removeZero(out)
        return out

    def adrv(self):
        'Anti-Derivative Helper Function'
        size = len(self.poly) + 1
        out = size * [0]
        div = size - 1
        index = 0
        while div > 0:
            out[index] = float(self.poly[index]) / float(div)
            div -= 1
            index += 1
        out[-1] = 0.0
        return out


    def drv(self):
        'Derivative via Power Rule: \
        d/dx(c*(x^n)) = (n*c) x^(n-1)'

        if len(self.poly) == 1:
            self.poly = [0]
        else:
            for i in range(len(self.poly)):
                if i < len(self.poly) - 1:
                    self.poly[i] *= len(self.poly) - (i+1)
                else:
                    #Pop if constant(i.e last element)
                    self.poly.pop(len(self.poly) - 1)

        print self.poly

    def __add__(self, other):
        'Overloader Addition operator'
        maxl = max(len(self.poly), len(other.poly))
        index = -1
        out = maxl * [0]

        while index >= (maxl*-1):
            if (index*-1) > len(self.poly):
                out[index] += other.poly[index]
            elif (index*-1) > len(other.poly):
                out[index] += self.poly[index]
            else:
                out[index] = self.poly[index] + other.poly[index]
            index -= 1
        out = self.removeZero(out)
        return polynom(out)

    def __sub__(self, other):
        'Overloader Addition operator'
        maxl = max(len(self.poly), len(other.poly))
        index = -1
        out = maxl * [0]

        while index >= (maxl*-1):
            if (index*-1) > len(self.poly):
                out[index] -= other.poly[index]
            elif (index*-1) > len(other.poly):
                out[index] -= self.poly[index]
            else:
                out[index] = self.poly[index] - other.poly[index]
            index -= 1
        out = self.removeZero(out)
        return polynom(out)

    def __mul__(self, other):
        'Overloaded multiplication operator'
        size = len(self.poly) + len(other.poly) - 1
        out = size * [0]
        for p0,c0 in enumerate(self.poly):
            for p1,c1 in enumerate(other.poly):
                out[p0+p1] += c0 * c1

        return polynom(out)


    def removeZero(self, input):
        #Suppress Leading Zeroes
        for i in range(len(input)):
            if input[i] == 0: continue
            elif input[i] != 0:
                input = input[i:]
                break
        return input