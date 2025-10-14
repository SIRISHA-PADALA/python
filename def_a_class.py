class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_started = False

    def start(self):
        if not self.is_started:
            print(f"The {self.year} {self.make} {self.model} is starting.")
            self.is_started = True
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_started:
            print(f"The {self.year} {self.make} {self.model} is stopping.")
            self.is_started = False
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

    def info(self):
        status = "running" if self.is_started else "stopped"
        print(f"\nCar Status: {self.year} {self.make} {self.model} is currently {status}.\n")


my_suv = Car("Honda", "CRV", 2020)

print("--- Starting Demonstration ---")

my_suv.info()

my_suv.start()
my_suv.info()

my_suv.start()

my_suv.stop()

my_suv.info()

print("--- Demonstration Complete ---")