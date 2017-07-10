from django.utils import timezone
from courses.models import Course, Lesson
from coaches.models import Coach
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


def coach_detail(request, pk):
    coach = get_object_or_404(Coach, pk=pk)
    courses = Course.objects.filter(coach=coach)
    assistant = Course.objects.filter(assistant=coach)
    return render(request, 'coaches/coach_detail.html', {'coach': coach,
                                                         'courses': courses,
                                                         'assistant': assistant})
