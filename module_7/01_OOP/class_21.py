class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass

class TraackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TraackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TraackedVehicle]:
        print(issubclass(cls1, cls2), end='\t')
    print()