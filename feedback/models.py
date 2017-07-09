from django.db import models


class FeedBackMessage(models.Model):
    mailer = models.CharField(max_length=50, verbose_name='name')
    email = models.EmailField(verbose_name='email')
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return "{email}: {text}".format(email=self.email, text=self.subject)
