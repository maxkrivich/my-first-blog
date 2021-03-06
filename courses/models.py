from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    coach = models.ForeignKey(
        'coaches.Coach', blank=True, null=True, related_name='coach_courses')
    assistant = models.ForeignKey(
        'coaches.Coach', blank=True, null=True, related_name='assistant_courses')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey('courses.Course', related_name='courses')
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.subject
