class Wall:
    armor = 10
    height = 5

    # write your code here
    
    # don't touch below this line
    def get_cost(self):
        return self.armor * self.height

    def fortify(self):
        self.armor *= 2 