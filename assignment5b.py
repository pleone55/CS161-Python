class Taxicab:
    def __init__(self, x_coord = 0, y_coord = 0):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.distance = 0
    
    """Getter methods"""
    def get_xcoord(self):
        return self.x_coord
    
    def get_ycoord(self):
        return self.y_coord
    
    def get_distance(self):
        return self.distance
    
    def moveX(self, dist_traveled):
        self.x_coord += dist_traveled
        self.distance += dist_traveled
    
    def moveY(self, dist_traveled):
        self.y_coord += dist_traveled
        self.distance += dist_traveled

cab1 = Taxicab(5, -8)
cab1.moveX(3)
cab1.moveY(-4)
cab1.moveX(-1)
print(cab1.get_distance())
print(cab1.get_ycoord())
print(cab1.get_xcoord())