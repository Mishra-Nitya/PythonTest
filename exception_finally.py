class AdultException(Exception):
    pass

class Person:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def display_person(self):
        try:
            print("the age is ", self.get_minor_age())
        except AdultException:
            print("person is an adult")
        finally:
            print("name is ", self.name)
    
    def get_minor_age(self):
        if self .age < 18:
            return self.age
        raise AdultException
    
a = Person('nitya', 12)
a.display_person()
       


