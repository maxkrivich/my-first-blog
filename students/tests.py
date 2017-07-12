import datetime
from django.test import TestCase, Client

from .models import Student


class StudentListTest(TestCase):
    def __generate_student(self, count=10):
        for i in range(count):
            Student.objects.create(name='name {}'.format(i),
                                   surname='surname {}'.format(i),
                                   date_of_birth='2002-11-11'.format(i),
                                   email='email{}@mail.com'.format(i),
                                   phone='123456789'.format(i),
                                   address='add{}'.format(i),
                                   skype='skype{}'.format(i))

    def setUp(self):
        self.__generate_student()

    def test_student_list_status_code(self):
        c = Client()
        response = c.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_count(self):
        self.assertEqual(Student.objects.all().count(), 10)


class CoursesDetailTest(TestCase):
    def setUp(self):
        Student.objects.create(name='Max',
                               surname='Krivich',
                               date_of_birth='2002-11-11',
                               email='test@mail.com',
                               phone='123456789',
                               address='asdad',
                               skype='skype')

    def test_student_db_is_not_empty(self):
        self.assertEqual(Student.objects.all().count(), 1)

    def test_student_full_name(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.full_name(), 'Krivich Max')

    def test_student_name(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.name, 'Max')

    def test_student_surname(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.surname, 'Krivich')

    def test_student_date_of_birth(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.date_of_birth, datetime.date(2002, 11, 11))

    def test_student_email(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.email, 'test@mail.com')

    def test_student_phone(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.phone, '123456789')

    def test_student_address(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.address, 'asdad')

    def test_student_skype(self):
        student = Student.objects.get(surname='Krivich')
        self.assertEqual(student.skype, 'skype')

    def test_student_detail_status_code(self):
        c = Client()
        response = c.get('/students/1')
        self.assertEqual(response.status_code, 200)

    def test_student_detail(self):
        student = Student.objects.all().first()
        c = Client()
        response = c.get('/students/1')
        self.assertContains(response, student.full_name())
        self.assertContains(response, student.skype)
        self.assertContains(response, student.email)

    def test_student_page_fails(self):
        c = Client()
        response = c.get('students/100/')
        self.assertEqual(response.status_code, 404)
