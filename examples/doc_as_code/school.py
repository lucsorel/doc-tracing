'''
source .venv/bin/activate
py2puml examples/doc_as_code examples.doc_as_code > examples/doc_as_code/doc_as_code.puml
'''
from dataclasses import dataclass

@dataclass
class Person:
    firstname: str
    lastname: str

@dataclass
class Course:
    name: str
    teacher: Person

@dataclass
class Student(Person):
    courses: list[Course]