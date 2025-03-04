# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels=4):
        self.num_wheels = num_wheels

    # drive method
    def drive(self):
        return (f'vroooom')


# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# Motorcycle

class Motorcycle(GroundVehicle):
    def __init__(self, num_wheels=2):
        super().__init__(num_wheels=2)

    # drive method
    def drive(self):
        return (f'BRAAAP!!')


vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# iterate through vehicles list
for vehicle in vehicles:
    # print drive() call on each vehicle
    print(vehicle.drive())

# print_drive = [vehicle.drive() for vehicle in vehicles]

# print_drive = list(map(lambda x: x.drive(), vehicles))

# print(print_drive)

