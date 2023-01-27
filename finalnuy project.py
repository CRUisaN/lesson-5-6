import random

class Human:
    def __init__(self, name="Human",subject=None):
        self.name = name
        self.gladness = 65
        self.satiety = 65
        self.knowledge = 30
        self.health = 60
        self.average_mark = 12
        self.marks = []
        self.subject = subject


    def eat(self):
        print("I`m eating")
        self.satiety += 20
        if self.satiety >= 100:
            self.satiety = 100
            return


    def chill(self):
        rest = random.randint(1,4)
        if rest == 1:
            print("Lets read book!")
            self.gladness += 10
        if rest == 2 or 3:
            print("---")
            print("Lets go fishing!")
            fishing = random.randint(1,4)
            if fishing == 1:
                print("---")
                print("Today i did not catch nothing")
                print("---")
                return
            if fishing == 2:
                print("---")
                print("I caught fish!")
                print("---")
                self.gladness += 10
            if fishing == 3:
                print("---")
                print("My fish broke!")
                print("---")
                self.gladness -= 1
            if fishing == 4:
                print("---")
                print("Oh, I stuck a hook in my finger!")
                print("---")
                self.health -= 1
                self.gladness -= 1
        if rest == 4:
            print("Lets walk!")
            self.gladness += 10
            self.health += 3


    def is_alive(self):
        if self.gladness < 0:
            print("         |---|---|")
            print("       --GAME OVER--")
            print("         |---|---|")
            print("       --|DEPRESION|--")
            print("         |---|---|")
            print("        --|AUTHOR|--")
            print("         |---|---|")
            print("  --|Лакуста Святослав|--")
            print("        --|1915|--")
            return False
        if self.health < 1:
            print("         |---|---|")
            print("       --GAME OVER--")
            print("         |---|---|")
            print("   --|DEaTH FROM DISEASE|--")
            print("         |---|---|")
            print("        --|AUTHOR|--")
            print("         |---|---|")
            print("  --|Лакуста Святослав|--")
            print("        --|1915|--")
            return False

    def live(self, day):
        if self.is_alive()==False:
            return False
        self.days_indexes(day)
        dice = random.randint(1,2)
        self.studing()
        self.eat()
        if self.health <= 10:
            print("I got sick!")
            self.satiety -= 10
            self.gladness -= 30
            self.health += 50
        if self.gladness < 20:
            print("Now rest")
            self.chill()
        if dice == 1:
            print("Snack time!")
            self.satiety += 5
            self.gladness += 10
            self.health -= 5
        elif dice == 2:
            print("Lets rest!")
            self.chill()


    def days_indexes(self, day):
        day = f"Today {day} day "
        print(f"{day:=^50}", "\n")
        human_indexes = "Stats"
        print(f"{human_indexes:^50}", "\n")
        print(f"Health - {self.health}")
        print(f"Satiety - {self.satiety}")
        print(f"Knowledge - {self.knowledge}")
        print(f"Average mark - {self.average_mark}")
        print(f"Gladness - {self.gladness}")
        print()


    def studing(self):
        print("|-----|Lets gnaw the granite of science!|-----|")
        subject_list = {
            "Chemistry": {"teaching": 40, "sadness": 10},
            "Physics": {"teaching": 35, "sadness": 8},
            "Foreign Languages": {"teaching": 25, "sadness": 4},
            "Native Language": {"teaching": 20, "sadness": 2},
            "Math": {"teaching": 30, "sadness": 6},
            "Biology": {"teaching": 21, "sadness": 5},
            "PE": {"teaching": 5, "sadness": 0},
            "Native History": {"teaching": 19, "sadness": 8},
            "History": {"teaching": 17, "sadness": 7}}
        for i in range(1,7):
            self.subject = random.choice(list(subject_list))
            self.teaching = subject_list[self.subject]["teaching"]
            self.sadness = subject_list[self.subject]["sadness"]
            print(f"   |------Lesson {self.subject}------|")
            self.knowledge += self.teaching
            self.gladness -= self.sadness
            self.satiety -= 5
            self.health -= 1
            self.mark = random.randint(1,12)
            self.marks.append(self.mark)
            print(f"   |------Mark: {self.mark} ------|")
            print(f"   |------ Break ------|")
            self.gladness += random.randint(1,4)
            self.satiety += 1



Human=Human(name="Human")
for day in range(1,11):
    if Human.live(day)==False:
        break