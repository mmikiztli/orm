from models import *
from datetime import date

# Populate random data with your models


def main():
    bp1 = CodecoolClass.create(location='Bp1', year=2017)
    bp1.save()
    Albert = Mentor.create(nickname='Albi',
                           first_name='Albert',
                           last_name='Einstein',
                           year_of_birth=date(1879, 3, 14),
                           gender='male',
                           codecool_class=bp1)
    Albert.save()

    Marti = Student.create(knowledge_level=10,
                           energy_level=1,
                           first_name='Marti',
                           last_name='Kecskemeti',
                           year_of_birth=date(1986, 3, 17),
                           gender='female',
                           codecool_class=bp1)
    Marti.save()


if __name__ == '__main__':
    main()
