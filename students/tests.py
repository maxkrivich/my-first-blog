import random
import datetime
from django.test import TestCase, Client

from .models import Student
from courses.models import Course
from courses.tests import CoursesFactory


class StudentFactory(object):

    def __init__(self):
        self.students = []

    def __generate_random_string(self, length=10):
        s = []
        for i in range(length):
            s.append(chr(random.randint(ord('A'), ord('z'))))
        return ''.join(s)

    def create_student(self):
        return Student.objects.create(name=self.__generate_random_string(),
                                      surname=self.__generate_random_string(),
                                      date_of_birth=datetime.datetime.now(),
                                      email=self.__generate_random_string() + '@mail.com',
                                      phone=str(random.randint(
                                          100000, 1000000000)),
                                      address=self.__generate_random_string(),
                                      skype=self.__generate_random_string())

    def create_students(self, count=10, clear=False):
        if clear:
            self.students = []

        for i in range(count):
            self.students.append(self.create_student())
        return self.students

    def add_student_on_course(self, course):
        if len(self.students):
            for i in range(3):
                stud = random.choice(self.students)


class StudentListTest(TestCase):

    def setUp(self):
        StudentFactory().create_students()

    def test_student_list_status_code(self):
        c = Client()
        response = c.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_count(self):
        self.assertEqual(Student.objects.all().count(), 10)

    def test_student_paginator_existing(self):
        c = Client()
        response = c.get('/students/?page=1')
        self.assertEqual(response.status_code, 200)

    def test_student_paginator_fails(self):
        c = Client()
        response = c.get('/students/?page=99999')
        self.assertEqual(response.status_code, 404)

    def test_student_on_course(self):
        pass


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
