from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_gender(self):
        pass 

class Male(Person):
    def get_gender(self):
        print("Male")

class Female(Person):
    def get_gender(self):
        print("Female")

male=Male()
male.get_gender()

female=Female()
female.get_gender()

p=Person()