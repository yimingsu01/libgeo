class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    

    def find_area(self):
        raise NotImplementedError

class Circle:
    def __init__(self, rad):
        self.radius = rad


