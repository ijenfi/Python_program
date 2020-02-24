import math
class Point:
    """class that knows x and y coordinates"""

    def __init__(self,start_x, start_y):
        """ Creating coordinates x and y """
        self.x = start_x
        self.y = start_y
    
    def get_X(self):
        #This method returns the value of coordinate x
        return self.x
    
    def get_Y(self):
        #This method returns the value of coordinate y
        return self.y

    
    #Implementing distance between two points
    def distance(self, pointA):
        diff_of_x = pointA.get_X() - self.get_X()
        diff_of_y = pointA.get_Y() - self.get_Y()

        dist = math.sqrt(diff_of_x**2 + diff_of_y**2)
        return dist

    

