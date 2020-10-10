

x1 = int(input("input x1:"))
y1 = int(input("input y1:"))
x2 = int(input("input x2:"))
y2 = int(input("input y2:"))





class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

        pass

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        distance = (((x1 + y1) ** 2) + ((x2 + y2) ** 2)) ** 0.5
        return distance

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        slope = (y2 - y1)/(x2 - x1)
        return slope



coordinate1 = (x1,y1)
coordinate2 = (x2,y2)

li = Line(coordinate1,coordinate2)


dist = li.distance()
sp = li.slope()
print (f"distance between two points are {dist}")
print(f"slope of the stright line is {sp}")


