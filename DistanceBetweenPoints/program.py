from coordinates import Point
from triangle import Triangle
def main():
    
   
    p_1 = Point(5, 4) #  instantiating new points
    p_2 = Point(7, 6)
    p_3 = Point(9, 8)
    
    
    getarea = triangle(p_1, p_2, p_3)
    print('The area is', getarea)


def distanceBetween(point1, point2):
    return point1.distance(point2)

def triangle(point1, point2, point3):
    triangle1 = Triangle(point1, point2, point3)
    return triangle1.getArea()


if __name__ == "__main__":
    main()