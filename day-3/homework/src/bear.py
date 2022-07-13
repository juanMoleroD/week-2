class Bear:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []
    
    def eat_fish(self, fish):
        self.stomach.append(fish)
    
    def count_food(self):
        return len(self.stomach)
    
    def eat_fish_from_river(self, river):
        self.stomach.append(river.take_fish()) 
    