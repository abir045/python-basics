class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Move along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')


# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()


you_car = Vehicle('Cadillac', 'Escalade')
you_car.get_make_model()
you_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along")


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along')


class GolfCart(Vehicle):

    pass


cesssna = Airplane('Cessna', "skyhawk", 'N-1234')
mack = Truck('Mack', "Pinnacle")
golfWagen = GolfCart('Yamaha', "GC100")


cesssna.get_make_model()
cesssna.moves()
mack.get_make_model()
mack.moves()
golfWagen.get_make_model()
golfWagen.moves()


print('\n\n')

for v in (my_car, you_car, cesssna, mack, golfWagen):

    v.get_make_model()
    v.moves()
