class Human:
    planet = "Earth" #static variable
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name ",self.name)
        print("Age ",self.age)
        print(Human.planet)

    @classmethod
    def display(cls):
        print("class method",cls.planet)

    @staticmethod
    def static_method():
        print(Human.planet)

h1 = Human("mg mg",20)
h2 = Human("ag ag",21)
Human.planet = "Mars"
h1.display()
h2.display()

# Human.static_method()