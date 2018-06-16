class Car:
    def __init__(self, **info):
        self.info = info

    def colour(self):
        return "{0}'s colour is Blue".format(self.info.get('name', 'Lada'))

    def nationality(self):
        return '{}\'s nationality is {}'.format(self.info.get('name', 'Lada'), self.info.get('nationality', 'Egyptian'))


class EuroCar(Car):
    def colour(self):
        return "{0}'s colour is Black".format(self.info.get('name', 'Lada'))
    pass


Mercedes = EuroCar(name="Mercedes", nationality="German")
print(Mercedes.colour())
print(Mercedes.nationality())
