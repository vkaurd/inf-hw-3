class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        print("Робот активирует лазер:", self.laser.does())
        print("Робот активирует клешню:", self.claw.does())
        print("Робот активирует смартфон:", self.smartphone.does())

my_robot = Robot()
my_robot.does()
