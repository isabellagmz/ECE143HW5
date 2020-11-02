# Isabella Gomez A15305555
# ECE143 HW5

class Interval(object):
    def __init__(self, a, b):
        """
        class represents open intervals on number line where a,b are x,y respectively

        :a: integer
        :b: integer
        """

        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)

        self._a = a
        self._b = b

    def __repr__(self):
        return 'Interval(%d, %d)'%(self._a,self._b)

    def __eq__(self, other):
        #check if the x coords are equal
        if self._a == other._a:
            # check if y coords are equal
            if self._b == other._b:
                return True

        # returns false if either is not equal
        return False

    def __lt__(self, other):
        # self and other do not overlap but self < other
        if self._a < other._a and self._b < other._a:
            return True
        if self._a < other._a and  self._b == other._a:
            return True
        return False

    def __gt__(self, other):
        # self and other do not overlap and self > other
        if self._a > other._a and self._a > other._b:
            return True
        if self._a > other._a and self._a == other._b:
            return True
        return False

    def __ge__(self, other):
        if self._a > other._a and self._a < other._b:
            return True
        return False

    def __le__(self, other):
        if self._a < other._a and other._a < self._b:
            return True
        return False

    def __add__(self, other):
        # checks if intervals are equal
        if self.__eq__(other):
            return self

        # check if self < other or self > other (do not overlap)
        if self.__lt__(other) or self.__gt__(other):
            return self, other

        # check if self <= other (do overlap)
        if self.__le__(other):
            # return [self.x, other.y] or [self.x, self.y]
            if self._b < other._b:
                return Interval(self._a, other._b)
            elif self._b > other._b or self._b == other._b:
                return Interval(self._a, self._b)

        # check if self >= other (do overlap)
        if self.__ge__(other) or self._a == other._a:
            if self._b > other._b:
                return Interval(other._a, self._b)
            elif other._b > self._b or self._b == other._b:
                return Interval(other._a, other._b)

