#!/usr/bin/env python

from enum import Enum
class Gender(Enum):
    MALE = 0
    FEMALE = 1
    TRANSGENDER = 2
    UNSPECIFIED = 3

class User:
    name = ""
    age = 0
    gender = Gender.UNSPECIFIED

    def display(self):
        if (self.gender == Gender.MALE):
            print self.name, 'is a male'
        elif (self.gender == Gender.FEMALE):
            print self.name, 'is a female'
        elif (self.gender == Gender.TRANSGENDER):
            print self.name, 'is transgender'
        else:
            print self.name, 'did not specify a gender'

user1 = User()
user1.name = 'Johnny'
user1.gender = Gender.TRANSGENDER

user2 = User()
user2.name = 'Rogelio'
user2.gender = Gender.MALE

user1.display()