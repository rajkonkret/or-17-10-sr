class Boat:
    """
    Dokumentacja
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # oznaczenie jako pole prywatne

    def sail(self):
        self.__speed += 20  # speed = speed + 20

    def speedometer(self):
        print("Speed in knots", self.__speed)


b1 = Boat("Omega", 2023)
b1.sail()
b1.sail()
b1.sail()
# print(b1.__speed)  # AttributeError: 'Boat' object has no attribute '__speed'
b1.speedometer()
# b1.__speed = 0
b1.speedometer()  # Speed in knots 0
# print(b1.__speed)
