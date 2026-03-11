class Student:
    _schoolName = 'XYZ School' # private class attribute 

    def __init__(self, name, age):
        self._name=name # private instance attribute

    def __display(self): # private method
        print('This is private method.')

std = Student("Bill", 25)
print(std._schoolName) 