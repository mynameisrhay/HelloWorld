# 13th exercise. using classes. must define a new type/class called Person which has a name attribute and talk method.

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, my name is {self.name}")


raymond = Person("Raymond Bautista")
raymond.talk()
