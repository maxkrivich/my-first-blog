from django.utils import timezone
from .models import FeedBackMessage
from .forms import FeedBackMessageFrom
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import mail_admins
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


class FeedbackView(CreateView):
    form_class = FeedBackMessageFrom
    model = FeedBackMessage
    template_name = 'feedback.html'
    success_url = '#'

    def get_context_data(self, **kwargs):
        return super(FeedbackView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form = super(FeedbackView, self).form_valid(form)
        message = "mailer: {mailer}\n\
                    email: {email}\n\
                    message: {message}\n\
                    date: {date}\n".format(mailer=self.object.mailer,
                                           email=self.object.email,
                                           message=self.object.message,
                                           date=self.object.date)
        mail_admins(self.object.subject, message, fail_silently=True)
        messages.success(
            self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        return form
