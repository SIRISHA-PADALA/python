class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# The Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class (Animal)
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} (a {self.breed}) barks: Woof! Woof!")

# The Cat class inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the parent class (Animal)
        super().__init__(name)
        self.color = color

    # Corrected method name and indentation
    def meow(self):
        print(f"{self.name} (a {self.color} cat) meows: Meow!")

# The Bird class inherits from Animal
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def fly(self):
        print(f"{self.name} (a {self.species}) is flying high!")

# --- Demonstration of Inheritance ---

print("\n--- Inheritance Demonstration ---")

# Create objects of the derived classes
my_dog = Dog("Buddy", "Siberian Husky")
my_cat = Cat("Whiskers", "Calico")
my_bird = Bird("Sky", "Pigeon")

# Dog demonstrating inherited and unique methods
my_dog.eat()    # Inherited from Animal
my_dog.bark()   # Unique to Dog
my_dog.sleep()  # Inherited from Animal

print("-" * 30)

# Cat demonstrating inherited and unique methods
my_cat.eat()    # Inherited from Animal
my_cat.meow()   # Unique to Cat
my_cat.sleep()  # Inherited from Animal

print("-" * 30)

# Bird demonstrating inherited and unique methods
my_bird.eat()   # Inherited from Animal
my_bird.fly()   # Unique to Bird
my_bird.sleep() # Inherited from Animal