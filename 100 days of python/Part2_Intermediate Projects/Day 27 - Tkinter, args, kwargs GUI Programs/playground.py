def add(*args):
    total = 0
    for num in args:
        total += num

    return total

print(add(1,2,3))

def calculate(n, **kwargs):
    # print(kwargs)
    for key,value in kwargs.items():
        # print(key)
        # print(value)
        # print(kwargs["add"])

        # n += kwargs["add"]
        # n *= kwargs["multiply"]
        # print(n)
        pass


calculate(2, add=3, multiply=5)

#calculate()


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

myCar = Car(make="Nissan", color = "Green")
print(myCar.color)