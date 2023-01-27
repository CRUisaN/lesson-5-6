import random

class Human:
    def __init__(self, name="Human",job=None, home=None,car=None,subject=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.knowledge=20
        self.job = job
        self.car = car
        self.home = home
        self.subject=subject
    def get_home(self):
        self.home=House()

    def get_car(self):
        self.car=Auto(brands_of_car = {
        "BMW": {"fuel": 100, "strength":100,"consumption": 6},
        "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
        "Volvo": {"fuel": 70, "strength": 150,"consumption": 8},
        "Ferrari": {"fuel": 80, "strength": 120,"consumption": 14}})

    def get_subject(self):
        self.subject=Study(subject_list = {
        "Math":{"teaching": 30, "sadness": 5},
        "English":{"teaching": 20, "sadness":3},
        "ICT":{"teaching": 15, "sadness": 2},
        "Pe":{"teaching": 3, "sadness": 1},
        "History": {"teaching": 25, "sadness": 7}})

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job=Job(job_list = {
        "Java developer":{"salary": 50, "gladness_less": 10},
        "Python developer":{"salary": 40, "gladness_less":3},
        "C++ developer":{"salary": 45, "gladness_less": 25},
        "Rust developer":{"salary": 70, "gladness_less": 1}})
    def eat(self):
        if self.home.food<=0:
            self.shopping("food")
        else:
            if self.satiety>=100:
                self.satiety=100
                return
            self.satiety+=5
            self.home.food-=5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money+=self.job.salary
        self.gladness-=self.job.gladness_less
        self.satiety-=4
    def studing(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.knowledge+=self.subject.teaching
        self.gladness-=self.subject.sadness
        self.satiety-=3

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel<20:
                manage="fuel"
            else:
                self.to_repair()
                return
        if manage=="fuel":
            print("Купив пальне")
            self.money-=100
            self.car.fuel+=100
        elif manage=="food":
            print("Купив їжу")
            self.money-=50
            self.home.food+=50
        elif manage=="delicious":
            print("Ура! Смачненьке!")
            self.gladness+=10
            self.satiety+=2
            self.money-=15

    def chill(self):
        self.gladness+=10
        self.home.mess+=5

    def clean_home(self):
        self.gladness-=5
        self.home.mess=0

    def to_repair(self):
        self.car.strength+=100
        self.money-=50

    def days_indexes(self, day):
        day=f"Today the {day} of {self.name}'a life"
        print(f"{day:=^50}","\n")
        human_indexes=self.name + "'s indexes"
        print(f"{human_indexes:^50}","\n")
        print(f"Money-{self.money}")
        print(f"Knowledge-{self.knowledge}")
        print(f"Satiety-{self.satiety}")
        print(f"Gladness-{self.gladness}")
        home_indexes="Home indexes"
        print(f"{home_indexes:^50}","\n")
        print(f"Food-{self.home.food}")
        print(f"Mess-{self.home.mess}")
        car_indexes=f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}","\n")
        print(f"Fuel-{self.car.fuel}")
        print(f"Strength-{self.car.strength}")

    def is_alive(self):
        if self.gladness<0:
            print("------------------------------------------")
            print("Дипресія")
            print("------------------------------------------")
            return False
        if self.satiety<0:
            print("------------------------------------------")
            print("Голод")
            print("------------------------------------------")
            return False
        if self.money<-500:
            print("------------------------------------------")
            print("Банкрот")
            print("------------------------------------------")
            return False

    def live(self, day):
        if self.is_alive()==False:
            return False
        if self.home is None:
            print("Переселися в будинок")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Я купив машину: {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Я не маю роботи, я йду отриматим роботу {self.job.job} з зарплатою {self.job.salary}")
        if self.subject is None:
            self.get_subject()
            print(f"Я вивчаю: {self.subject.subject}")
        self.days_indexes(day)
        dice=random.randint(1,5)
        if self.satiety<20:
            print("Я йду їсти")
            self.eat()
        elif self.gladness<20:
            if self.home.mess>15:
                print("Я хочу відпочити, але в будинку брудно \n Тож я піду прибирати будинок")
                self.clean_home()
            else:
                print("Я відпочиваю")
                self.chill()
        elif self.money<0:
            print("Я йду працювати")
            self.work()
        elif self.knowledge<90:
            print("Я йду вчитися")
            self.studing()
        elif self.car.strength<15:
            print("Мені потрібно відремонтувати машину")
            self.to_repair()
        elif dice==1:
            print("Давайте відпочинемо")
            self.chill()
        elif dice==2:
            print("Початок роботи")
            self.work()
        elif dice==3:
            print("Час прибирання")
            self.clean_home()
        elif dice==4:
            print("Час смачненького")
            self.shopping(manage="delicacies")
        elif dice==5:
            print("Пора вчитися")
            self.studing()
class Auto:
    def __init__(self, brands_of_car):
        self.brand = random.choice(list(brands_of_car))
        self.fuel = brands_of_car[self.brand]["fuel"]
        self.strength = brands_of_car[self.brand]["strength"]
        self.consumption = brands_of_car[self.brand]["consumption"]

    brands_of_car = {
        "BMW": {"fuel": 100, "strength":100,"consumption": 6},
        "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
        "Volvo": {"fuel": 70, "strength": 150,"consumption": 8},
        "Ferrari": {"fuel": 80, "strength": 120,"consumption": 14}}

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self,job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]
    job_list = {
        "Java developer":{"salary": 50, "gladness_less": 10},
        "Python developer":{"salary": 40, "gladness_less":3},
        "C++ developer":{"salary": 45, "gladness_less": 25},
        "Rust developer":{"salary": 70, "gladness_less": 1}}

class Study:
    def __init__(self,subject_list):
        self.subject=random.choice(list(subject_list))
        self.teaching=subject_list[self.subject]["teaching"]
        self.sadness=subject_list[self.subject]["sadness"]
    subject_list = {
        "Math":{"teaching": 30, "sadness": 5},
        "English":{"teaching": 20, "sadness":3},
        "ICT":{"teaching": 15, "sadness": 2},
        "Pe":{"teaching": 3, "sadness": 1},
        "History": {"teaching": 25, "sadness": 7}}


nick=Human(name="Nick")
for day in range(1,8):
    if nick.live(day)==False:
        break