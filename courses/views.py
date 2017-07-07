from django.utils import timezone
from courses.models import Course, Lesson
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def course_detail(request, pk):
    if Course.objects.filter(pk=pk).exists():
        # TODO написать проверку есть ли в курсе уроки
        return render(request, 'courses/course_detail.html', {'course': Course.objects.get(pk=pk),
        'lesson': Lesson.objects.filter(course=pk).order_by("order"),})
    else:
        return HttpResponse('404')
