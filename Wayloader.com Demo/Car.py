class Car:
    def __init__(self, brand, model, year , Address):
        self.brand = brand
        self.model = model
        self.year = year
        self.Address = Address

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}" f" {self.Address}")

# Creating objects (instances) of the class
car1 = Car("Toyota", "Corolla", 2023 , "swabi")
car2 = Car("Honda", "Civic", 2022, "gulberg green")

# Calling the method
car1.display_info()
car2.display_info()

