# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:46:52 2021

@author: Aungp
"""

class Student:
    def __init__(self, student_id, name, age, city, phone):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.city = city
        self.phone = phone

student = Student(1,'Mg Mg', 23, 'Yangon', '09774511562')
print(student)
