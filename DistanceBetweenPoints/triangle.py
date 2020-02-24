import math
class Triangle():
        def __init__(self, P1, P2, P3):
        
            self.p1 = P1
            self.p2 = P2
            self.p3 = P3
        
        def getArea(self):
            lenghtP1P2 = self.p1.distance(self.p2)
            lenghtP1P3 = self.p1.distance(self.p3)
            lenghtP2P3 = self.p2.distance(self.p3)
            lenght = lenghtP1P2 + lenghtP1P3 + lenghtP2P3
            
            print('The sum of the sides lenght is:', lenght)
            
            semiperimeter = lenght / 2
            
            area = math.sqrt(semiperimeter * (semiperimeter * lenghtP1P2) * (semiperimeter * lenghtP1P3) * (semiperimeter * lenghtP2P3))
            return area