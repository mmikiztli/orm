from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase('marti', user='marti')


class BaseModel(Model):

    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class Person(BaseModel):

    '''Person'''
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    year_of_birth = DateField()
    gender = CharField(max_length=255)


class CodecoolClass(BaseModel):

    '''CodecoolClass'''
    location = CharField(max_length=255)
    year = IntegerField()

    def mentors(self):
        return self.mentors_list

    def students(self):
        return self.students_list


class Student(Person):

    '''Student'''
    knowledge_level = IntegerField()
    energy_level = IntegerField()
    codecool_class = ForeignKeyField(
        CodecoolClass, related_name='students_list')


class Mentor(Person):

    '''Mentor'''
    nickname = CharField(max_length=255)
    codecool_class = ForeignKeyField(
        CodecoolClass, related_name='mentors_list')
