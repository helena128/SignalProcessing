# Class that draws the chart

class Drawer:
    def __init__(self, points):
        self.points = points

    def draw(self):
        print(len(self.points))
        for key, value in self.points.items():
            print("x={}; y={}".format(str(key),str(value)))

#points = {1:1.5, 2: 2.5, 3:0, 4:0}
#drawer = Drawer(points)
#drawer.draw()

#TODO: add drawing
