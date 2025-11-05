class Car:
    def __init__(self, make, model, year):  # Corrected __init__
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.year} {self.make} {self.model} is starting")

    def stop(self):
        print(f"The {self.year} {self.make} {self.model} is stopped")


# Creating objects
car1 = Car("TOYOTA", "LANDCRUISER", 2024)
car2 = Car("TOYOTA", "LANDCRUISER", 2034)

# Using the methods
car1.start()
car2.stop()
