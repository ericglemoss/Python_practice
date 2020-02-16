import matplotlib.pyplot as plt
import numpy as np


class Polygon:

    def __init__(self,name='Standard triangle',coordinates=[[0,1],[-1,0],[1,-0]],regular=False,sides=3):
        Polygon.sides = sides
        Polygon.regular = regular
        Polygon.name = name
        Polygon.coordinates = coordinates

    def __len__(self):
        return "This polygon has {}".format(self.sides)

    def info(self):
            if self.regular:
                return "The polygon {} has {} sides and it is regular".format(self.name, self.sides)
            else:
                return "The polygon {} has {} sides and is not regular.".format(self.name, self.sides)

    def __del__(self):
        return "The polygon {} was deleted.".format(self.name)

    def display(self):
        tmp = self.coordinates
        tmp.append(tmp[0])
        xs, ys = zip(*tmp)
        plt.figure()
        plt.plot(xs, ys)
        plt.show()


    def polygon_area(self):
        sum_1 = 0
        sum_2 = 0

        for i in range(len(self.coordinates)-1):
            sum_1 += self.coordinates[i][0]*self.coordinates[i+1][1]
            sum_2 += self.coordinates[i][1]*self.coordinates[i+1][0]
        sum_1 += self.coordinates[len(self.coordinates)-1][0]*self.coordinates[0][1]
        sum_2 += self.coordinates[len(self.coordinates)-1][1]*self.coordinates[0][0]

        return 0.5*abs(sum_1 - sum_2)

