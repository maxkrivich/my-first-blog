from django.db import models


class Coach(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField('auth.User')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    skype = models.CharField(max_length=20)
    description = models.TextField()

    @property
    def is_staff(self):
        return self.user.is_staff

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def __str__(self):
        return "{} {}".format(self.user.last_name, self.user.first_name)
