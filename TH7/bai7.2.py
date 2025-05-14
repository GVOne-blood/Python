class Vehicle:
    def __init__(self, make):
        self.make = make

    def description(self):
        print(self.make)


class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model

    def description(self):
        print(f'{self.make} \t {self.model}')


class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def description(self):
        print(f'{self.make} \t {self.model} \t {self.battery_size}')


veh = Vehicle('Honda')
veh.description()

car = Car('Honda', 'Honda PX5')
car.description()

ecar = ElectricCar('Honda', 'Honda PX5', '300000mAh')
ecar.description()
