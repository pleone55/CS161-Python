class Box:
    def __init__(self, height=1, width=1, length=1):
        self.height = height
        self.width = width
        self.length = length
    
    """Setter Methods"""
    def set_height(self, height):
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_length(self, length):
        self.length = length
    
    """Getter Methods"""
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width

    def get_length(self):
        return self.length
    
    def calculate_volume(self):
        return self.height * self.width * self.length
    
    def calc_surface_area(self):
        return ((2 * self.length * self.width) + (2 * self.length * self.height) + (2 * self.height * self.width))

box1 = Box(23, 4, 12)
box2 = Box()

print(box1.calculate_volume())
print(box1.calc_surface_area())
print(box2.calculate_volume())
print(box2.calc_surface_area())