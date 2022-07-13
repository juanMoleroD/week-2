class River:
    
    def __init__(self, name):
        self.name = name
        self.fish_in_river = []

    def add_fish(self, fish):
        self.fish_in_river.append(fish)
    
    def fish_count(self):
        return len(self.fish_in_river)

    def take_fish(self):
        return self.fish_in_river.pop()
        