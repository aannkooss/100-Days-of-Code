class Animal:
    alive = True
    def eat(self):
        print("The animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.sleep() #No need to use print function, since this calls a function that already prints something
hawk.eat()
