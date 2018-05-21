from math import sqrt, fabs as module

class Polygon:

    def __init__(self, *args, sides_num):
        '''
        constructor method for polygon parent class, it takes *args as unlimited number of listf with 2 ints
        checks if 3 dots are not on the same line
        checks if user entered a proper amount of points for a specific figure
        '''
        self.sides_num = sides_num
        self.coords = [*args]
        self.per = 0
        self.s = 0
        self.all_sides = []
        for i in range(0, len(self.coords) - 1):
            self.all_sides.append(Polygon.side_len(self.coords[i], self.coords[i + 1]))
        self.all_sides.append(Polygon.side_len(self.coords[0], self.coords[-1]))
        if len(self.coords) != self.sides_num:
            raise Exception ("Unproper number of coordinates for current figuretype")
        if ((self.coords[1][1] - self.coords[0][1])/(self.coords[1][0] - self.coords[0][0]) == (self.coords[2][1] - self.coords[0][1])/(self.coords[2][0] - self.coords[0][0])):
            raise Exception ("3 of points u entered, are on the same line")

    @staticmethod
    def side_len(coord1, coord2):
        '''
        takes 2 coordinates, return length of a line between points
        '''
        return sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

    def perimeter(self):
        '''
        return perimeter of a figure
        '''
        for i in range(0, len(self.coords) - 1):
            self.per += Polygon.side_len(self.coords[i], self.coords[i+1])
        self.per += Polygon.side_len(self.coords[0], self.coords[-1])
        return self.per

    def area(self):
        '''
        return figures area
        '''
        for i in range(0, len(self.coords) - 1):
            self.s += self.coords[i][0] * self.coords[i+1][1]
            self.s -= self.coords[i+1][0] * self.coords[i][1]
        self.s += self.coords[-1][0] * self.coords[0][1]
        self.s -= self.coords[0][0] * self.coords[-1][1]
        self.s = 0.5 * module(self.s)
        return self.s

class Triangle(Polygon):

    def __init__(self, *args, sides_num):
        '''
        inherith from parent class Polygon spicifies a number of sides
        '''
        super().__init__(*args, sides_num = 3)


class Quadrilateral(Polygon):

    def __init__(self, *args, sides_num):
        '''
        inherith from parent class Polygon, spicifies a number of sides
        '''
        super().__init__(*args, sides_num = 4)

class Pentagon(Polygon):

    def __init__(self, *args, sides_num):
        '''
        inherith from parent class Polygon, spicifies a number of sides
        '''
        super().__init__(*args, sides_num = 5)

class Hexagon(Polygon):

    def __init__(self, *args, sides_num):
        '''
        inherith from parent class Polygon, spicifies a number of sides
        '''
        super().__init__(*args, sides_num = 6)

class Octagon(Polygon):

    def __init__(self, *args, sides_num):
        '''
        inherith from parent class Polygon, spicifies a number of sides
        '''
        super().__init__(*args, sides_num = 8)

class IsoscelesTriangle(Triangle):

    def __init__(self,  *args, sides_num):
        '''
        inherith from parent class Triengle
        checks if endered points of triangle make 2 lines with the same length
        '''
        super().__init__(*args, sides_num=3)
        if self.all_sides[0] != self.all_sides[1] and self.all_sides[0] != self.all_sides[2] and self.all_sides[1] != self.all_sides[2]:
            raise Exception ("This triangle is not Isosceles")
        if self.all_sides[0] == self.all_sides[1] and self.all_sides[0] == self.all_sides[2] and self.all_sides[1] == self.all_sides[2]:
            raise Exception ("This triangle is not Isosceles")

class EquilateralTriangle(Triangle):

    def __init__(self,  *args, sides_num):
        '''
        inherith from parent class Triengle
        checks if endered points of triangle make 3 lines with the same length
        '''
        super().__init__(*args, sides_num=3)
        if not(self.all_sides[0] == self.all_sides[1] and self.all_sides[0] == self.all_sides[2] and self.all_sides[1] == self.all_sides[2]):
            raise Exception ("This triangle is not Equilateral")

class Rectangle(Quadrilateral):
    def __init__(self, *args, sides_num):
        '''
        inherith from parent class Quadrilateral
        checks if endered points of triangle make 2 lines with the same length, and 2 other lines with the same length
        '''
        super().__init__(*args, sides_num = 4)
        self.all_sides.sort()
        if not(self.all_sides[0] == self.all_sides[1] and self.all_sides[2] == self.all_sides[3] and self.all_sides[2] != self.all_sides[3]):
            raise Exception ("These are not a Rectangle coordinates")


class Square(Quadrilateral):
    def __init__(self, *args, sides_num):
        '''
        inherith from parent class Quadrilateral
        checks if endered points of triangle make 4 lines with the same length
        '''
        super().__init__(*args, sides_num = 4)
        if not (self.all_sides[0] == self.all_sides[1] and self.all_sides[1] == self.all_sides[2] and self.all_sides[2] == self.all_sides[3] and self.all_sides[0] == self.all_sides[3]):
            raise Exception ("These are not a square coordinates")


q = Hexagon([1, 2], [5, 2], [3, 4], [2, 1], [6, 5], [7, 4], sides_num=6)
print(q.perimeter())
print(q.area())