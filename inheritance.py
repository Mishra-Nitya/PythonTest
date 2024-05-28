class Animal:
    def __init__(self) -> None:
        pass
    def habitat(self):
        print("this is the method for animal class")
class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
    def habitat(self):
        print("this is the method for dog class")
d = Dog()
d.habitat()
