class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octopus:
    def eats(self):
        return 'campers'

# создаем по 1 реальному объекту каждого класса
bear_obj = Bear()
rabbit_obj = Rabbit()
octopus_obj = Octopus()

# вызываем методы
print("медведь ест:", bear_obj.eats())
print("кролик ест:", rabbit_obj.eats())
print("осьминог ест:", octopus_obj.eats())
