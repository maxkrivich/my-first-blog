from django.test import TestCase, Client

from .models import Course, Lesson
from coaches.models import Coach


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
