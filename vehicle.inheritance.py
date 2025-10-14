class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.is_running = False

    def start_engine(self):
        if not self.is_running:
            print(f"The {self.make} {self.model}'s engine is starting.")
            self.is_running = True
        else:
            print(f"The {self.make} {self.model} is already running.")

    def stop_engine(self):
        if self.is_running:
            print(f"The {self.make} {self.model}'s engine is shutting down.")
            self.is_running = False
        else:
            print(f"The {self.make} {self.model} is already off.")

class Truck(Vehicle):
    def __init__(self, make, model, max_load):
        super().__init__(make, model)
        self.max_load = max_load
        self.current_load = 0

    def load_cargo(self, weight):
        if self.current_load + weight <= self.max_load:
            self.current_load += weight
            print(f"Loaded {weight} kg. Total load is now {self.current_load} kg.")
        else:
            print(f"Cannot load {weight} kg. Max load of {self.max_load} kg exceeded.")

    def haul(self):
        if self.is_running and self.current_load > 0:
            print(f"The {self.model} is hauling its {self.current_load} kg load.")
        elif not self.is_running:
            print("Start the engine first!")
        else:
            print("Nothing to haul! The truck is empty.")


# Execution Block
my_truck = Truck("Ford", "F-150", 1500)

print("--- Truck Operation Demo ---")

my_truck.start_engine()
my_truck.load_cargo(1000)
my_truck.haul()
my_truck.stop_engine()

print("\n--- Next Operation ---")
my_truck.start_engine()
my_truck.load_cargo(600)
my_truck.stop_engine()