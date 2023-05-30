from _pytest.python_api import raises

from nyoibo import Entity, fields
from nyoibo.exceptions import RequiredValueError


def test_simple():
    class Person(Entity):
        _first_name = fields.StrField()
        _last_name = fields.StrField()

    class Student(Person):
        _school = fields.StrField()

    first_name = 'test name'
    last_name = 'test last name'
    school = 'MIT'
    student = Student(
        first_name=first_name,
        last_name=last_name,
        school=school
    )

    assert student.first_name == first_name
    assert student.last_name == last_name
    assert student.school == school


def test_multiple():
    class Person(Entity):
        _first_name = fields.StrField()
        _last_name = fields.StrField()

    class Citizen(Entity):
        _identification = fields.StrField()

    class Student(Citizen, Person):
        _school = fields.StrField()

    first_name = 'test name'
    last_name = 'test last name'
    friends = ('some friend name', 'another friend name')
    school = 'MIT'
    identification = '123456789'
    student = Student(
        first_name=first_name,
        last_name=last_name,
        friends=friends,
        school=school,
        identification=identification
    )

    assert student.first_name == first_name
    assert student.last_name == last_name
    assert student.school == school
    assert student.identification == identification


def test_deeper():
    class Grandma(Entity):
        _name = fields.StrField()

    class Mother(Grandma):
        _profession = fields.StrField()

    class Child(Mother):
        _toys = fields.TupleField()

    name = 'test name'
    profession = 'stundent'
    toys = ('test toy', 'second test toy')
    child = Child(
        name=name,
        profession=profession,
        toys=toys
    )

    assert child.name == name
    assert child.profession == profession
    assert child.toys == toys


def test_redefine_field():
    class Parent(Entity):
        _value = fields.StrField(required=True)
        _whatever = fields.StrField()

    class Child(Parent):
        _whatever = fields.StrField(required=True)

    with raises(RequiredValueError):
        Child(value='some value')
