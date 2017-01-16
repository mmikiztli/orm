import unittest
from datetime import date
from models import *


class Tester(unittest.TestCase):

    def test_db_connection(self):
        result = db.connect()
        self.assertEqual(result, None)

    def test_ccclass_model(self):
        bp1 = CodecoolClass.create(location='Bp1', year=2016)
        self.assertEqual(type(bp1).__name__, 'CodecoolClass')

    def test_person_model(self):
        bp2 = CodecoolClass.create(location='Bp2', year=2016)
        bob = Person.create(
            first_name='Bob',
            last_name='Marley',
            year_of_birth=date(1945, 2, 6),
            gender='male',
            codecool_class=bp2
        )
        self.assertEqual(type(bob).__name__, 'Person')
        bob_loaded = Person.get(Person.first_name == 'Bob' and Person.last_name == 'Marley')
        self.assertEqual(bob_loaded.year_of_birth, date(1945, 2, 6))

    def test_mentor_model(self):
        bp3 = CodecoolClass.create(location='Bp3', year=2016)
        mentor = Mentor.create(
            nickname='boby',
            first_name='Mentor',
            last_name='Marley',
            year_of_birth=date(1966, 2, 6),
            gender='male',
            codecool_class=bp3
        )
        self.assertEqual(type(mentor).__name__, 'Mentor')
        self.assertEqual(len(bp3.mentors()), 1)

    def test_student_model(self):
        bp4 = CodecoolClass.create(location='Bp4', year=2016)
        student = Student.create(
            knowledge_level=10,
            energy_level=1,
            first_name='John',
            last_name='Doe',
            year_of_birth=date(1991, 1, 1),
            gender='male',
            codecool_class=bp4
        )
        self.assertEqual(type(student).__name__, 'Student')
        student2 = Student.create(
            knowledge_level=11,
            energy_level=1,
            first_name='July',
            last_name='Doe',
            year_of_birth=date(1992, 2, 1),
            gender='female',
            codecool_class=bp4
        )
        self.assertEqual(type(student2).__name__, 'Student')
        self.assertEqual(len(bp4.students()), 2)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
