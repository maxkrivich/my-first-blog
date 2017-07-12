from django.test import TestCase, Client

from .models import Course


class CourseListTest(TestCase):
    def setUp(self):
        for i in range(10):
            Course.objects.create(name='Course {}'.format(i),
                                  short_description='qwerty123{}'.format(i),
                                  description='ytrewq3{}21'.format(i))

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

    def test_course_name(self):
        course = Course.objects.get(short_description='qwerty1234')
        self.assertEqual(course.name, 'Course 4')

    def test_course_short_description(self):
        course = Course.objects.get(name='Course 5')
        self.assertEqual(course.short_description, 'qwerty1235')

    def test_course_description(self):
        course = Course.objects.get(name='Course 5')
        self.assertEqual(course.description, 'ytrewq3521')

    # TODO write test for assistant and coach
