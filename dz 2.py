class Cat:
    def __init__(self, name="Cat", home=None, health=100):
        self.name = name
        self.gladnes = 100
        self.satiety = 100
        self.food = 10
        self.home = home
        self.health = health
    def  get_home(self):
        self.home = Huose()
        self.energy = 100

    def eat(self):
        if self.food <= 0:
            self.found.food("I need found food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.energy += 20
            self.food -= 5

    def founding_food(self, manage):
        if self.energy >= 10:
            self.found.food("Food")
        else:
            if manage == "food":
                print("I found food")
                self.food += 5
                self.energy -= 10
