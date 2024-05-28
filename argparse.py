class AdultException(Exception):
    pass

class Person:

    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age
    
    def get_minor_age(self):        
        if self.age<18:
            print("they are a minor")
        else:
            raise AdultException
    def display(self):
        try:
            print(f'age -> {self.get_minor_age()}')
        except AdultException:
            print("they are an adult")
        finally:
            print(self.name, self.age)

a = Person("nitya", 12)
a.display()

