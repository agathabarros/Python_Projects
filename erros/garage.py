class Car:
    def __init__(self, make, model):
        self.marke = make
        self.model = model
    
    def __repr__(self) -> str:
        return f'<Car {self.make} {self.model}>'
    
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):  #ask for permission
            raise TypeError(f'Tried to add `{car.__class__.__name__}` to the garage, but you can only add...')
        self.cars.append(car)
        
ford = Garage()
fiesta = Car('Ford', 'Fiesta')

try:
    ford.add_car(fiesta)
except TypeError:
    print('your car was not a Car!')

