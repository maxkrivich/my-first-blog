import datetime
import random

from django.test import TestCase, Client
from django.contrib.auth.models import User

from .models import Course, Lesson
from coaches.models import Coach


class Util(object):
    def generate_random_string(self, length=10):
        s = []
        for i in range(length):
            s.append(chr(random.randint(ord('A'), ord('z'))))
        return ''.join(s)


class CoachFactory(Util):

    def create_coach(self):
        return Coach.objects.create(
            user=User.objects.create(username=super(
                CoachFactory, self).generate_random_string()),
            date_of_birth=datetime.datetime.now(),
            gender=random.choice(['M', 'F']),
            phone=super(CoachFactory, self).generate_random_string(),
            address=super(CoachFactory, self).generate_random_string(),
            skype=super(CoachFactory, self).generate_random_string(),
            description=super(CoachFactory, self).generate_random_string(),
        )

    def create_coachs(self, count=10):
        coaches = []
        for i in range(count):
            coaches.append(self.create_coach())
        return coaches


class LessonFactory(Util):

    def create_lesson(self, course=None):
        return Lesson.objects.create(subject=super(CoachFaLessonFactoryctory, self).generate_random_string(),
                                     description=super(
                                         LessonFactory, self).generate_random_string(),
                                     course=course,
                                     order=random.randint(1, 100))


class CoursesFactory(Util):
    def __init__(self):
        self.courses = []

    def create_course(self, coach=None, assistant=None):
        return Course.objects.create(name=super(CoursesFactory, self).generate_random_string(),
                                     short_description=super(
                                         CoursesFactory, self).generate_random_string(),
                                     description=super(
                                         CoursesFactory, self).generate_random_string(),
                                     coach=coach, assistant=assistant)


class CourseListTest(TestCase):
    def setUp(self):
        for i in range(10):
            Course.objects.create(name='Course {}'.format(i),
                                  short_description='qwerty123{}'.format(i),
                                  description='ytrewq3{}21'.format(i))

    def test_cource_fail(self):
        c = Client()
        response = c.get('cources/1111/')
        self.assertEqual(response.status_code, 404)

    def test_course_status_code(self):
        c = Client()
        response = c.get('/courses/')
        self.assertEqual(response.status_code, 200)


class CourseDetailTest(TestCase):
    def setUp(self):
        for i in range(10):
            Course.objects.create(name='Course {}'.format(i),
                                  short_description='qwerty123{}'.format(i),
                                  description='ytrewq3{}21'.format(i))

    def test_course_status_code(self):
        c = Client()
        response = c.get('/courses/1')
        self.assertEqual(response.status_code, 200)

    def test_course_page_fails(self):
        c = Client()
        response = c.get('cources/4000/')
        self.assertEqual(response.status_code, 404)

    def test_course_name(self):
        course = Course.objects.get(short_description='qwerty1234')
        self.assertEqual(course.name, 'Course 4')

    def test_course_short_description(self):
        course = Course.objects.get(name='Course 5')
        self.assertEqual(course.short_description, 'qwerty1235')

    def test_course_description(self):
        course = Course.objects.get(name='Course 5')
        c = Client()
        response = c.get('/cources/{}/'.format(course.pk))
        self.assertContains(response, course.name)
        self.assertContains(response, course.short_description)
        self.assertContains(response, course.description)

    # TODO write test for assistant and coach
