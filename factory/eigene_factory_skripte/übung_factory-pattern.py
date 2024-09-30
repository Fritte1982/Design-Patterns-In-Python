from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def drive(self):
        pass
    
class Car(Vehicle):
    
    def drive(self):
        return "Car is driving"
    
class Bike(Vehicle):
    
    def drive(self):
        return "Bike is driving"
    
class VehicleFactory():
    
    @staticmethod
    def choice_vehicle( v_type:str):
        if v_type.lower() =="car":
            return Car()
        elif v_type.lower() == "bike":
            return Bike()
        else:
            raise ValueError(f"Type {v_type} is nicht in der Fabrik vorhanden")

def main():
    car =VehicleFactory.choice_vehicle("Car")
    print(car.drive())


    
if __name__ == '__main__':
    main()        