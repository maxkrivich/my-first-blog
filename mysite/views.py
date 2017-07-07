from django.utils import timezone
from courses.models import Course, Lesson
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def get_home_page(request):
    course = Course.objects.all()
    return render(request, 'home.html', {'courses': course})


def get_contact(request):
    return render(request, 'contact.html', {})
