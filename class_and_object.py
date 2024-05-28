class Employee:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
emp = Employee(1, "coder")
n = Employee(2, "nitya")
print(emp.name)
del emp.id
print(n.id)
#print(emp.id)
del emp

