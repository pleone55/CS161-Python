class Player:
    def __init__(self, name = "", points = -100, rebounds = -100, assists = -100):
        self.name = name
        self.points = points
        self.rebounds = rebounds
        self.assists = assists
    
    """Getter Methods"""
    def get_name(self):
        return self.name
    
    def get_points(self):
        return self.points
    
    def get_rebounds(self):
        return self.rebounds
    
    def get_assists(self):
        return self.assists
    
    """Setter Methods"""
    def set_name(self, name):
        self.name = name
    
    def set_points(self, points):
        self.points = points
    
    def set_rebounds(self, rebounds):
        self.rebounds = rebounds
    
    def set_assists(self, assists):
        self.assists = assists
    
    def has_more_points(self, player) -> bool:
        if self.get_points() > player.get_points():
            return True
        return False

class Team():
    def __init__(self, p1, p2, p3, p4, p5):
        self.set_point_guard(p1)
        self.set_shooting_guard(p2)
        self.set_small_forward(p3)
        self.set_power_forward(p4)
        self.set_center(p5)
    
    """Setter Methods"""
    def set_point_guard(self, point_guard):
        self.point_guard = point_guard
    
    def set_shooting_guard(self, shooting_guard):
        self.shooting_guard = shooting_guard
    
    def set_small_forward(self, small_forward):
        self.small_forward = small_forward
    
    def set_power_forward(self, power_forward):
        self.power_forward = power_forward
    
    def set_center(self, center):
        self.center = center
    
    """Getter Methods"""
    def get_point_guard(self):
        return self.point_guard
    
    def get_shooting_guard(self):
        return self.shooting_guard
    
    def get_small_forward(self):
        return self.small_forward
    
    def get_power_forward(self):
        return self.power_forward
    
    def get_center(self):
        return self.center
    
    def total_points(self):
        return self.get_point_guard().get_points() + self.get_shooting_guard().get_points() + self.get_small_forward().get_points() + self.get_power_forward().get_points() + self.get_center().get_points()

p1 = Player("Paul", 24, 10, 7)
p2 = Player("Jon", 13, 4, 1)
p3 = Player("Jane", 10, 8, 8)
p4 = Player("Josh", 20, 6, 7)
p5 = Player("Kyle", 8, 12, 10)
p5.set_points(10)

team1 = Team(p1, p2, p3, p4, p5)

p = team1.get_shooting_guard()
total = team1.total_points()
print(p.get_name())
print(total)
print(p4.has_more_points(p1))