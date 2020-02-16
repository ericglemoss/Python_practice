import math
import matplotlib.pyplot as plt


class Dot:
    def __init__(self,name='Standard point on origin',x=0,y=0):
        Dot.x = x
        Dot.y = y
        Dot.name = name

    def coordinates(self):
        return (self.x, self.y)

    def distance_to_origin(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def distance_to_other_point(self,dot_b):
        return math.sqrt((self.x - dot_b.x)**2 + (self.y - dot_b.y)**2)

    def realocate(self,x_new,y_new):
        Dot.x = x_new
        Dot.y = y_new

    def dot_name(self):
        return self.name

    def display(self):
        plt.plot(self.x,self.y,'r*',markersize=3.5)
        plt.show()

